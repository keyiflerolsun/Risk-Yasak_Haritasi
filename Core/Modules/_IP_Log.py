# Bu Araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from httpx     import Client as Session
from httpx     import Timeout
from aiocached import cached

@cached
async def ip_log(hedef_ip:str) -> dict[str, str]:
    oturum = Session(
        headers = {
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        },
        timeout = Timeout(10, connect=10, read=5*60, write=10)
    )

    istek = oturum.get(f"http://ip-api.com/json/{hedef_ip}").json()

    if istek["status"] != "fail":
        return {
            "ulke"   : istek["country"] or "",
            "il"     : istek["regionName"] or "",
            "isp"    : istek["isp"] or "",
            "sirket" : istek["org"] or "",
            "host"   : istek["as"] or ""
        }
    else:
        return {"hata": "Veri Bulunamadı.."}