# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Core  import api_v1
from flask import jsonify

from Public.API.v1.Libs import risk_veri

@api_v1.route("/risk", methods=["GET", "POST"])
async def risk():
    veri = await risk_veri()

    return jsonify(veri), 200