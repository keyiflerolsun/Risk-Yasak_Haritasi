# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import render_template, jsonify, request, abort

@app.route('/')
def ana_sayfa():

    return render_template(
        'harita.html',
        baslik = "Covid-19 Risk Yasak Haritası",
    )

from KekikFlask.risk_datasi import risk_durumlari

@app.route('/veri', methods=['POST'])
def veri():
    gelen_data   = request.form.to_dict()
    data_kontrol = bool((gelen_data) and ('nak_nak' in gelen_data.keys()) and (gelen_data['nak_nak']) == '@KekikAkademi')
    xhr_kontrol  = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if xhr_kontrol and data_kontrol:
        return jsonify(risk_durumlari())
    else:
        abort(403)