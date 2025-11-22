from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "<p>About Page</p>"


@app.route("/ciao")
def ciao():
    name = request.args.get("name", "Flask")
    return f"<p>Ciao, {escape(name)}!</p>"


@app.route("/hello?name=<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.get("/data/<chi>")
def data_chi(chi):
    return {
        "name": chi,
        "age": 30,
        "city": "New York"
    }


if __name__ == "__main__":
    app.run(debug=True)
