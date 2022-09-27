from flask import Blueprint

from .views import (
    only_admin, product, secret,
    getusers, addsession, sendmessage, viewcontacts
)

bp = Blueprint("webui", __name__, template_folder="templates")

# bp.add_url_rule("/whatschat/allusers", view_func=getusers)
# viewcontacts
bp.add_url_rule("/", view_func=getusers)
bp.add_url_rule("/whatschat", view_func=getusers)
bp.add_url_rule(
    "/whatschat/addsession",
    view_func=addsession, endpoint="addsession",
    methods=["GET", "POST"]
)
bp.add_url_rule(
    "/whatschat/sendmessage/<username>",
    view_func=sendmessage, endpoint="sendmessage",
    methods=["GET", "POST"]
)
bp.add_url_rule(
    "/whatschat/viewcontacts/<username>",
    view_func=viewcontacts, endpoint="viewcontacts",
    methods=["GET", "POST"]
)

bp.add_url_rule(
    "/product/<product_id>",
    view_func=product, endpoint="productview"
)
bp.add_url_rule("/secret", view_func=secret, endpoint="secret")
bp.add_url_rule(
    "/only_admin",
    view_func=only_admin, endpoint="onlyadmin"
)


def init_app(app):
    app.register_blueprint(bp)
