from flask import Flask, url_for, request

app = Flask(__name__)

app.config["APP_NAME"] = "My Blog"


@app.errorhandler(404)
def not_found_page(error):
    return f"Not Found on {app.config['APP_NAME']}"



@app.route("/")
def index():
    content_url = url_for("read_content", title="Novidades de 2024")
    return (
        f"<h1>{app.config['APP_NAME']}</h1>"
        f"<a href='{content_url}'>Novidades de 2024</a>"
        "<hr>"
        f"{request.method}"
    )


@app.route("/<title>")
def read_content(title):
    index_url = url_for("index")
    return "<h1>{title}</h1> <a href='{index_url}'>Votar</a>"



# executar dentro do bloco
if __name__ == "__main__":
    app.run(debug=True)
