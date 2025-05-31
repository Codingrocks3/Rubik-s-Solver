from cube import *
import flask
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode
app.config['SECRET_KEY'] = 'itsnotrubix'  # Replace with a secure key

cube = Cube()

@app.route("/index")
@app.route("/")
def index():
    return flask.render_template("cube.html")

@app.route("/_turn")
def turn():
    algo = flask.request.args.get("move") or flask.request.args.get("algorithm") or ""
    cube.algorithm(algo)
    return flask.jsonify({"cube": cube.cube_state})

if __name__ == "__main__":
    app.run()