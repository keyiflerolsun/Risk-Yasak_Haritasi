# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Core           import app
from flask          import jsonify
from flask_wtf.csrf import CSRFError

@app.errorhandler(404)
async def dort_yuz_dort(error):
    return jsonify(hata="Sayfa Bulunamadı.."), 404

@app.errorhandler(403)
async def dort_yuz_uc(error):
    return jsonify(hata="Bu Sayfaya Erişim İzniniz Yoktur..!"), 403

@app.errorhandler(410)
async def dort_yuz_on(error):
    return jsonify(hata="Sayfa Taşınmış Olabilir.."), 410

@app.errorhandler(500)
async def bes_yuz(error):
    return jsonify(hata="Düzgün Argüman Verilmedi.. » (Sunucu Hatası Oluştu!)"), 500

@app.errorhandler(CSRFError)
async def csrf_hata(error):
    return jsonify(hata="CSRF Hatası"), 500

# * Favicon

# from flask import send_from_directory
# from os    import path

# @app.get("/favicon.ico")
# async def favicon():
#     try:
#         return send_from_directory(directory=path.join(app.root_path, "Static"), filename="favicon.ico", mimetype="image/x-icon")
#     except TypeError:
#         return send_from_directory(directory=path.join(app.root_path, "Static"), path="favicon.ico", mimetype="image/x-icon")