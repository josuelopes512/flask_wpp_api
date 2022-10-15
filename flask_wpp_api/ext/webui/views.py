from flask import (
    abort, render_template, request, url_for, redirect
)
from flask_simplelogin import login_required

from flask_wpp_api.models import Product
from .controller import Chat, Session

chat = Chat()
session = Session()

# def index():
#     products = Product.query.all()
#     return render_template("index.html", products=products)


# def product(product_id):
#     product = Product.query.filter_by(id=product_id).first() or abort(
#         404, "produto nao encontrado"
#     )
#     return render_template("product.html", product=product)


def getusers():
    return render_template(
        "chat.html", 
        sessions=session.get_all_users()
    )


def addsession():
    data = {
        "qrcode": "", "error": "",
        "success": "", "message": "",
        "cadastro": True,
        "username": "", "contact": ""
    }
    if request.method == 'POST':
        username = request.form['username']
        data["username"] = username
        result = session.create_new_session(username)
        
        if "qrcode" in result:
            data["qrcode"] = result["qrcode"]
            return render_template("adduser.html", data=data)
        else:
            data["error"] = result['error']
            return render_template("adduser.html", data=data)
    return render_template("adduser.html", data=data)


def sendmessage(username):
    data = {"qrcode": "", "error": "", "success": "", "message": True,
            "cadastro": "", "username": username, "contact": ""}
    if request.method == 'POST':
        number = request.form['number']
        message_text = request.form['message']
        
        result = chat.send_text(username, number, message_text)
        
        if 'success' in result:
            data["success"] = result['success']
            pass
        else:
            data["error"] = result['error']
        return render_template("adduser.html", data=data)
    elif not session.is_session_exists(username):
        return redirect(url_for("webui.addsession"))
    return render_template("adduser.html", data=data)


def viewcontacts(username):
    data = {"qrcode": "", "error": "", "success": "", "message": "",
            "cadastro": "", "username": username, "contact": ""}
    if not session.is_session_exists(username):
        return redirect(url_for("webui.addsession"))
    
    return render_template("adduser.html", data=data)


# @login_required
# def secret():
#     return "This can be seen only if user is logged in"


# @login_required(username="admin")
# def only_admin():
#     return "only admin user can see this text"
