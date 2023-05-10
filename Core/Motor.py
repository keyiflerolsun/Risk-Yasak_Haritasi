# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI               import konsol
from Core              import app
from waitress          import serve as waitress_serve
from hypercorn.config  import Config
from hypercorn.asyncio import serve as hypercorn_serve
from requests          import get
from Settings          import AYAR
from sys               import version_info

async def basla():
    global_ip = get("https://ipapi.co/json/").json().get("ip") or get("https://api64.ipify.org").text or "127.0.0.1"

    # global_ip = "127.0.0.1"

    if ":" in global_ip:
        global_ip = f"[{global_ip}]"

    surum = f"{version_info[0]}.{version_info[1]}"
    konsol.print(f"\n[bold gold1]{AYAR['PROJE']}[/] [yellow]:bird:[/] [turquoise2]Python {surum}[/] [bold yellow2]{AYAR['APP'].get('SERVE')}[/]", width=70, justify="center")
    konsol.print(f"[red]{global_ip}[light_coral]:[/]{AYAR['APP'].get('PORT')}[pale_green1] başlatılmıştır...[/]\n", width=70, justify="center")

    match AYAR["APP"].get("SERVE"):
        case "flask":
            import logging
            log = logging.getLogger("werkzeug")
            log.setLevel(logging.ERROR)
            app.run(debug=False, host="::", port=AYAR["APP"].get("PORT"), threaded=True)
        case "waitress":
            waitress_serve(app, listen=f"*:{AYAR['APP'].get('PORT')}")
        case "hypercorn":
            from asgiref.wsgi import WsgiToAsgi

            config          = Config()
            config.loglevel = "error"
            config.bind     = f"[::]:{AYAR['APP'].get('PORT')}"

            await hypercorn_serve(app=WsgiToAsgi(app), config=config, mode="asgi")
        # case "gevent":
        #     from gevent.pywsgi import WSGIServer
        #     gevent_server = WSGIServer(listener=("::", AYAR["APP"].get("PORT")), application=app, log=None)
        #     gevent_server.serve_forever()