from flask import render_template, request
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template(
        "index.html"
    )


@bp.route("/home")
def home():
    return render_template(
        "home.html", 
        name=request.args['name']
    )

@bp.route("/restaurantes")
def restaurants():
    return render_template(
        "restaurants.html"
    )