from flask import abort, render_template, url_for, redirect

def index():
    return render_template("index.html")