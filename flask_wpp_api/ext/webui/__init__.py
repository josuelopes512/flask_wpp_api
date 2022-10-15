from flask import Blueprint

from .views import (
    getusers, addsession, sendmessage, viewcontacts
)

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=getusers, endpoint='home')
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


def init_app(app):
    app.register_blueprint(bp)
