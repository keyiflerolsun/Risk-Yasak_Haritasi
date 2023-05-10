# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import Request
from json  import loads

def req_veri(request:Request) -> dict:
    get_params = request.args.to_dict() if request.args else None
    post_json  = loads(request.data.decode("utf-8")) if request.data else None
    post_data  = request.form.to_dict() if request.form else None

    return get_params or post_json or post_data or {}