from flask import Blueprint
from .views import index

bp = Blueprint("webwhatsapp", __name__, template_folder="templates")

bp.add_url_rule("/wpp", view_func=index)

def init_app(app):
    app.register_blueprint(bp)