#FLASK
from flask import Flask, jsonify, render_template, request
import os,optparse,sys, yaml
app = Flask(__name__)

environment="development"

with open("cv.yaml", "r") as f:
    curriculum = yaml.load(f, Loader=yaml.FullLoader)
    print(type(curriculum))


@app.route("/cv")
def cv():
    return render_template("cv.html", cv=curriculum)


@app.route("/cowsay")
def cow():
    return sys.exec("cowsay 'hello from flask'")

@app.route("/links")
@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", cv=curriculum)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0",debug=debug)
