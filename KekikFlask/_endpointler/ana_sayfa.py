# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template

@app.route('/')
def ana_sayfa():

    return render_template(
        'harita.html',
        baslik = "Covid-19 Risk - Yasak Haritası",
    )