# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikFlask import app
from flask import jsonify, request, abort
from Yardimcilar import risk_durumlari

@app.route('/veri', methods=['POST'])
def veri():
    gelen_data   = request.form.to_dict()
    data_kontrol = bool((gelen_data) and ('nak_nak' in gelen_data.keys()) and (gelen_data['nak_nak']) == '@KekikAkademi')
    xhr_kontrol  = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if xhr_kontrol and data_kontrol:
        return jsonify(risk_durumlari())
    else:
        abort(403)