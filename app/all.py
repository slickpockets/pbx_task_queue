from flask import current_app, Blueprint
import os
from .tasks import make_file

bp = Blueprint("all", __name__)
@bp.route("/")
def index():
    return "hello"
@bp.route("/<string:fname>/<string:content>")
def makefile(fname, content):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    make_file.delay(fpath, content)
    return(f"find your file @ <code>{fpath}</code>")
