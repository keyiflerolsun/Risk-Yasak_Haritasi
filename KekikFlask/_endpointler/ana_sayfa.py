# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template, jsonify

@app.route('/')
def ana_sayfa():

    return render_template(
        'harita.html',
        baslik = "Covid-19 Risk Yasak Haritası",
    )

from KekikFlask.risk_datasi import risk_durumlari

@app.route('/veri', methods=['GET', 'POST'])
def veri():
    return jsonify(risk_durumlari())