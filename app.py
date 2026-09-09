"""
Exercice de page de détails
"""

from flask import Flask, render_template, request

import bd
from config import Config

config = Config()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.jinja")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=config.APP_ENV.lower() == "local")
