from flask import current_app, Blueprint, render_template, request
import os
from .tasks import make_file, requester

bp = Blueprint("all", __name__)
@bp.route("/")
def index():
    return "hello"

@bp.route("/<string:fname>/<string:content>")
def makefile(fname, content):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    make_file.delay(fpath, content)
    return(f"find your file @ <code>{fpath}</code>")

@bp.route("/sms", methods=["POST"])
def test(message, phonenumbers):
    message = request.get["message"]
    phonenumbers = request.get["phonenumbers"]
    requester.delay(message, phonenumbers)
    return("test sent to task queue")

@bp.route("/portal")
def portal():
    return render_template("portal.html")
