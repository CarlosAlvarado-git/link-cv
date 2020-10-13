#FLASK
from flask import Flask, jsonify, render_template, request
import os,optparse,sys
app = Flask(__name__)

environment="development"

links={
    "Facebook": "https://facebook.com",
    "Twitter": "https://twitter.com"
}


@app.route("/cv")
def cv():
    return render_template("cv.html", links=links)


@app.route("/links")
@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", links=links)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0",debug=debug)
