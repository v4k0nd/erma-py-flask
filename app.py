import os
import json
from collections import defaultdict
from flask import (
    Blueprint,
    Flask,
    jsonify,
    render_template,
    send_from_directory,
    redirect,
)
from flask_assets import Environment, Bundle
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


database_url = os.environ.get("DATABASE_URL", "default_database_url")
secret_key = os.environ.get("SECRET_KEY")
domain = os.environ.get("DOMAIN")
# base_url = os.environ.get("APP_BASE_URL")

ro_blueprint = Blueprint("ro", __name__, url_prefix="/ro")
hu_blueprint = Blueprint("hu", __name__, url_prefix="/hu")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+mysqlconnector://ermaro_viewer:{secret_key}@{database_url}/ermaro_catalogs"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.debug = True


CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "https://www.example.com"}})

db = SQLAlchemy(app)

assets = Environment(app)

css = Bundle(
    "css/catalog-setup.css",
    "css/styles.css",
    filters="cssmin",
    output="css/packed/packed.css",
)

# Bundle for JavaScript
# js = Bundle(
#     'js/jquery.min.js',
#     'js/bootstrap.min.js',
#     'js/custom.js',
#     filters='jsmin',
#     output='packed/packed.js'
# )

# Register the bundles with Flask-Assets
assets.register("css_all", css)
# assets.register('js_all', js)

image_urls = [
    f"https://{domain}/images/1szn15.jpg",
    f"https://{domain}/images/1ind15.jpg",
    f"https://{domain}/images/5bv.jpg",
]


class Catalog(db.Model):
    __tablename__ = "catalogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    image = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP)
    type = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)


@app.route("/")
def index():
    # Redirect to the default language homepage
    return redirect("/ro/")


@ro_blueprint.route("/")
def ro_home():
    lang = "ro"
    active_catalogs = Catalog.query.filter_by(active=True).all()
    catalogs_by_type = defaultdict(list)
    for catalog in active_catalogs:
        catalogs_by_type[catalog.type].append(catalog)
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(
        f"{lang}/home.html", catalogs_by_type=catalogs_by_type, **translations
    )


@ro_blueprint.route("/about")
def ro_about():
    lang = "ro"
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(f"{lang}/about.html", **translations)


# @ro_blueprint.route("/gallery")
# def ro_gallery():
#     lang = "ro"
#     with open(f"translations/{lang}.json") as f:
#         translations = json.load(f)
#     return render_template(f"{lang}/gallery.html", images=image_urls, **translations)


@ro_blueprint.route("/contact")
def ro_contact():
    lang = "ro"
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(f"{lang}/contact.html", **translations)


@hu_blueprint.route("/")
def hu_home():
    lang = "hu"
    active_catalogs = Catalog.query.filter_by(active=True).all()
    catalogs_by_type = defaultdict(list)
    for catalog in active_catalogs:
        catalogs_by_type[catalog.type].append(catalog)
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(
        f"{lang}/home.html", catalogs_by_type=catalogs_by_type, **translations
    )


@hu_blueprint.route("/about")
def hu_about():
    lang = "hu"
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(f"{lang}/about.html", **translations)


# @hu_blueprint.route("/gallery")
# def hu_gallery():
#     lang = "hu"
#     with open(f"translations/{lang}.json") as f:
#         translations = json.load(f)
#     return render_template(f"{lang}/gallery.html", images=image_urls, **translations)


@hu_blueprint.route("/contact")
def hu_contact():
    lang = "hu"
    with open(f"translations/{lang}.json") as f:
        translations = json.load(f)
    return render_template(f"{lang}/contact.html", **translations)


app.register_blueprint(ro_blueprint)
app.register_blueprint(hu_blueprint)

if __name__ == "__main__":
    app.run()
