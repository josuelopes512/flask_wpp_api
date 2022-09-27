from flask import abort, render_template, request, url_for, redirect
from flask_simplelogin import login_required

from flask_wpp_api.models import Product

import requests as req
import json


def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)


def getusers():
    res = req.get('http://127.0.0.1:8000/sessions/getAll')
    if res.status_code == 200:
        data = res.json()
        return render_template("chat.html", sessions=data["data"])
    return render_template("chat.html", sessions=[])


def addsession():
    data = {"qrcode": "", "error": "", "success": "", "message": "",
            "cadastro": True, "username": "", "contact": ""}
    error_alert = "Session already exists, please use another username."
    if request.method == 'POST':
        username = request.form['username']
        data["username"] = username
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = f"id={username}&isLegacy=false"
        res = req.post('http://127.0.0.1:8000/sessions/add',
                       headers=headers, data=payload)
        if res.status_code == 200:
            data_res = res.json()
            data["qrcode"] = data_res["data"]["qr"]
            return render_template("adduser.html", data=data)
        else:
            data["error"] = error_alert
            return render_template("adduser.html", data=data)
    return render_template("adduser.html", data=data)


def isusername(username):
    res = req.get(f"http://127.0.0.1:8000/sessions/find/{username}")
    if res.status_code == 200:
        return True
    return False


def sendmessage(username):
    data = {"qrcode": "", "error": "", "success": "", "message": True,
            "cadastro": "", "username": username, "contact": ""}
    if not isusername(username):
        return redirect(url_for("webui.addsession"))
    if request.method == 'POST':
        # username = request.form['username']
        number = request.form['number']
        message_text = request.form['message']
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "receiver": f"{number}",
            "message": {
                "text": message_text
            }
        }
        res = req.post(
            f"http://127.0.0.1:8000/chats/send?id={username}",
            headers=headers, data=json.dumps(payload)
        )
        print(res.content.decode("utf8"))
        if res.status_code == 200:
            data_res = res.json()
            if data_res["success"]:
                data["success"] = "The message has been successfully sent."
                return render_template("adduser.html", data=data)
            else:
                data["error"] = "Failed to send the message."
                return render_template("adduser.html", data=data)
        else:
            data["error"] = "Failed to send the message."
            return render_template("adduser.html", data=data)
    return render_template("adduser.html", data=data)


def viewcontacts(username):
    data = {"qrcode": "", "error": "", "success": "", "message": "",
            "cadastro": "", "username": username, "contact": ""}
    if not isusername(username):
        return redirect(url_for("webui.addsession"))

    return render_template("adduser.html", data=data)


@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
