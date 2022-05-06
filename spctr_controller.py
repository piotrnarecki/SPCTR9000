from flask import Flask, render_template, abort, request, url_for, flash, redirect

# ...
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
    if request.method == 'POST':

        messages = [{'title': 'Message One',
                     'content': 'Message One Content'},
                    {'title': 'Message Two',
                     'content': 'Message Two Content'}
                    ]

        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for("show_form"))

    if request.method == 'GET':
        return render_template("spctr_load_data.html")


@app.route("/analyse_data")
def analyse_data():
    return render_template("spctr_results.html")

    # return render_template('form_test.html')
    # wyslij do BE

    # odbierz od BE

    # wyslij na FE


@app.route("/export_results")
def export_results():
    return "Data exported"


@app.route("/get_input", methods=["GET", "POST"])
def get_input():
    if request.method == "POST":

        smooth_type = request.form['smooth_radio']
        smooth_window_size = request.form['smooth_window_size']
        range = request.form['range_radio']

        print("INPUT:")

        print(smooth_type)
        print(smooth_window_size)
        print(range)

        if range == "custom_range":
            range_from = request.form['range_from']
            range_to = request.form['range_to']
            print(range_from)
            print(range_to)

        return redirect(url_for("export_results"))


    else:
        return render_template("get_input.html")
