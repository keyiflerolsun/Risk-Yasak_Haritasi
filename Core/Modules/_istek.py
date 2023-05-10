# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI         import konsol
from Core        import app
from flask       import g, request, session, Response
from time        import time
from user_agents import parse

from Core.Modules._IP_Log import ip_log
from Core.Modules         import req_veri

@app.before_request
async def istekten_once():
    g.start = time()

@app.after_request
async def istekten_sonra(yanit:Response) -> Response:
    for path in ("/favicon.ico", "/Static", "/webfonts"):
        if path in request.path:
            return yanit

    simdi = time()

    try:
        if str(parse(request.headers.get("User-Agent"))).split("/")[2].strip() == "Other":
            cihaz = request.headers.get("User-Agent")
        else:
            cihaz = parse(request.headers.get("User-Agent"))
    except TypeError:
        cihaz = request.headers.get("User-Agent")

    log_ip = request.environ.get("HTTP_X_FORWARDED_FOR") or request.environ.get("REMOTE_ADDR") or request.remote_addr

    log_veri = {
        "id"     : session.get("kullanici_id") or "", 
        "method" : request.method,
        "url"    : request.host_url[:-1] + request.full_path.rstrip("?").split("?")[0],
        "veri"   : req_veri(request),
        "kod"    : yanit.status_code,
        "sure"   : round(simdi - g.start, 2) if g.get("start") else 0,
        "ip"     : f"{request.headers.get('Cf-Connecting-Ip')} [yellow]| CF: ({log_ip})[/]" if request.headers.get("Cf-Connecting-Ip") else log_ip,
        "cihaz"  : cihaz,
        "host"   : request.host.split(":", 1)[0],
    }

    if request.headers.get("X-Request-ID"):
        log_veri["id"] = request.headers.get("X-Request-ID")

    endpoint_bilgisi = f"[bold blue]»[/] [bold turquoise2]{log_veri['url']}[/]"
    data_bilgisi     = f"[blue]|[/] [green]veri:[/] [bold turquoise2]{log_veri['veri']}[/]" if log_veri["veri"] else ""

    konsol.log(f"{endpoint_bilgisi} {data_bilgisi}")
    konsol.log(f"[bold bright_blue]{log_veri['id']}[/][bold green]@[/][bold red]{log_veri['ip']}[/]\t[blue]|[/] [green]cihaz:[/] [magenta]{log_veri['cihaz']}[/] [blue]|[/] [bold green]{log_veri['method']}[/] [blue]-[/] [bold bright_yellow]{log_veri['kod']}[/] [blue]-[/] [bold yellow2]{log_veri['sure']}sn[/]")

    ip_detay = await ip_log(log_veri["ip"].split()[0])
    if ("hata" not in list(ip_detay.keys())) and (ip_detay["ulke"]):
        konsol.log(f"[bold chartreuse3]{ip_detay['ulke']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['il']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['sirket']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['isp']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['host']}[/]")

    return yanit