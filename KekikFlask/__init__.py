# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi KekikFlask",
    aciklama = "KekikFlask Başlatıldı..",
    banner   = "KekikFlask",
    girinti  = 4
)

konsol = taban.konsol

def onemli(yazi):
    konsol.print(yazi, style="bold cyan", width=70, justify="center")

from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

app.config["JSON_SORT_KEYS"]                       = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"]          = True
app.config["JSON_AS_ASCII"]                        = False
app.config["SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS"] = True

from requests import get
from parsel import Selector
from json import dumps

def ip_log(hedef_ip:str):
    url    = f"https://whatismyipaddress.com/ip/{hedef_ip}"
    istek  = get(url).text
    secici = Selector(istek)

    bilgi_alani = secici.xpath("//div[@class='ip-information']")

    return {
        'host'     : bilgi_alani.xpath("//span[text()='Hostname:']/following-sibling::span//text()").get(),
        'isp'      : bilgi_alani.xpath("//span[text()='ISP:']/following-sibling::span//text()").get(),
        'baglanti' : bilgi_alani.xpath("//span[text()='Type:']/following-sibling::span//text()").get(),
        'gorev'    : bilgi_alani.xpath("//span[text()='Assignment:']/following-sibling::span//text()").get(),
        'ulke'     : bilgi_alani.xpath("//span[text()='Country:']/following-sibling::span//text()").get(),
        'il'       : bilgi_alani.xpath("//span[text()='State/Region:']/following-sibling::span//text()").get()
    }


from time import time
from flask import g, request
from user_agents import parse

@app.before_request
def zamanlayici_baslat():
    g.start = time()

@app.after_request
def istek_log(yanit):
    if (request.path == "/favicon.ico") or (request.path.startswith("/static")):
        return yanit

    simdi = time()

    if str(parse(request.headers.get('User-Agent'))).split('/')[2].strip() == 'Other':
        cihaz = request.headers.get('User-Agent')
    else:
        cihaz = parse(request.headers.get('User-Agent'))

    log_veri = {
        'id'     : '', 
        'method' : request.method,
        'url'    : request.host_url[:-1] + request.full_path,
        'data'   : request.form.to_dict(),
        'kod'    : yanit.status_code,
        'sure'   : round(simdi - g.start, 2),
        'ip'     : request.remote_addr,
        'cihaz'  : cihaz,
        'host'   : request.host.split(":", 1)[0],
    }

    if request.headers.get("X-Request-ID"):
        log_veri.update({"id" : request.headers.get("X-Request-ID")})

    ip_detay = ip_log(log_veri['ip'])
    konsol.log(f"[bold blue]»[/] [bold turquoise2]{log_veri['url']}[/] [blue]|[/] [green]data:[/] [bold turquoise2]{log_veri['data']}[/]")
    konsol.log(f"[bold bright_blue]{log_veri['id']}[/][bold green]@[/][bold red]{log_veri['ip']}[/]\t[blue]|[/] [green]cihaz:[/] [magenta]{log_veri['cihaz']}[/] [blue]|[/] [bold green]{log_veri['method']}[/] [blue]-[/] [bold bright_yellow]{log_veri['kod']}[/] [blue]-[/] [bold yellow2]{log_veri['sure']}sn[/]")
    konsol.log(f"[bold chartreuse3]{ip_detay['ulke']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['il']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['isp']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['baglanti']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['gorev']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['host']}[/]")

    return yanit

####
from KekikFlask._endpointler import _hata, ana_sayfa