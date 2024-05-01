from flask import url_for
from app import app, mongo


@app.errorhandler(404)
def not_found_page(error):
    return f"Not found on {app.config['APP_NAME']}"


@app.route("/")
def index():
    posts = mongo.db.posts.find()

    content_url = url_for("read_content", title="Novidades de 2024")
    return 