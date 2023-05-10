# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Core  import home
from flask import render_template

@home.get("/")
async def ana_sayfa():
    return render_template(
        "index.html",
        baslik   = "Covid-19 Risk - Yasak Haritası",
        aciklama = "keyiflerolsun - Ömer Faruk Sancak | KekikAkademi » siz hayal edin, biz geliştirelim.. 🕊"
    )