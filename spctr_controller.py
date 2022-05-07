from flask import Flask, render_template, abort, request, url_for, flash, redirect

# ...
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

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


@app.route("/load_data", methods=['GET', 'POST'])
def load_data():
    if request.method == "POST":

        smooth_type = request.form['smooth_radio']
        smooth_window_size = request.form['smooth_window_size']
        range = request.form['range_radio']

        print("INPUT:")

        print(smooth_type)
        print(smooth_window_size)
        print(range)

        baseline = request.form['baseline_radio']
        print(baseline)


        if range == "custom_range":
            range_from = request.form['range_from']
            range_to = request.form['range_to']
            print(range_from)
            print(range_to)




        return redirect(url_for("export_results"))


    else:
        return render_template("spctr_load_data.html")



@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if request.files['file'].filename != '':
            file = request.files['file']
            file.save(secure_filename(file.filename))
            print(file.filename)
            return 'file uploaded successfully'
        else:
            return redirect(url_for("load_data"))


@app.route("/analyse_data", methods=['GET', 'POST'])
def analyse_data():
    return render_template("spctr_results.html")

    # return render_template('form_test.html')
    # wyslij do BE

    # odbierz od BE

    # wyslij na FE


@app.route("/export_results")
def export_results():
    return "Data exported"

