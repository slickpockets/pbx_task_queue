from flask import current_app, Blueprint, render_template, request, redirect
import os
from .tasks import requester

bp = Blueprint("all", __name__)
@bp.route("/")
def index():
    return "hello"



@bp.route("/sms", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        message = request.form.get("message")
        if not message:
            message = request.get["message"]
            if not message:
                return("no message")

        phonenumbers = request.form.get("phonenumbers")
        if not phonenumbers:
            phonenumbers = request.get["phonenumbers"]
            if not phonenumbers:
                return("no phone numbers")

        password = request.form.get("password")
        if not password:
            password = request.get["password"]
            if not password:
                return("no password")

        requester.delay(message, phonenumbers, password)
        return("done")
    else:
        return redirect('/portal')



@bp.route("/portal")
def portal():
    return render_template("portal.html")
