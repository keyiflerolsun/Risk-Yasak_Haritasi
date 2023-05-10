# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

# ! BluePrintler
from flask import Flask, Blueprint

app = Flask(__name__)

home = Blueprint(
    name            = "Home",
    import_name     =  __name__,
    url_prefix      = "/",
    template_folder = "../Public/Home/Templates",
    static_folder   = "../Public/Home/Static"
)

api_v1 = Blueprint(
    name        = "API_v1",
    import_name = __name__,
    url_prefix  = "/api/v1"
)


# ! Flask Konfigürasyonları
from flask_sitemap  import Sitemap
from flask_wtf.csrf import CSRFProtect
from os             import urandom

ext = Sitemap(app=app)

app.secret_key = urandom(16)
app.json_provider_class.ensure_ascii               = False
app.json_provider_class.sort_keys                  = False
app.json_provider_class.compact                    = False
app.config["SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS"] = True
app.config["WTF_CSRF_ENABLED"]                     = True
app.config["WTF_CSRF_METHODS"]                     = {"GET", "POST", "PUT", "PATCH", "DELETE"}

csrf = CSRFProtect(app)

# ! ----------------------------------------» Routers
from Core.Modules          import _istek, _hata, req_veri
from Public.Home.Routers   import ana_sayfa
from Public.API.v1.Routers import risk

app.register_blueprint(home)
csrf.exempt(home)               # ? CSRF'e Dahil Etme
app.register_blueprint(api_v1)