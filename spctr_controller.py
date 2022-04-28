from flask import Flask, render_template, abort
from model import db


# WPISZ PONISZE KOMENTY W TERMINAL NA DOLE ABY URUCHOMIC
# export FLASK_APP=spctr9000_controller.py
# export FLASK_ENV=developer
# export FLASK_DEBUG=1
# flask run




app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("spctr_welcome.html")

@app.route("/load_data")
def load_data():
    return render_template("spctr_load_data.html")


@app.route("/analyse_data")
def analyse_data():
    return render_template("spctr_results.html")


@app.route("/export_results")
def export_results():
    return "Data exported"

