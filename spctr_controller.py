from flask import Flask, render_template, abort, request, url_for, flash, redirect

# ...
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from frontend_utils.input_interpreter import InputInterpreter
from frontend_utils.input_parameters import InputParameters
from frontend_utils.file_interpreter import FileInterpreter

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

        input_interpreter = InputInterpreter()

        # input_parameters - obiekt tej PRZEPIEKNEJ klasy zawiera wszystkie parametry do obliczen
        input_parameters = input_interpreter.interpret_params(request)

        # dziala !
        print("INPUT DZIALA " + input_parameters.deconvolution_type)  # tak zeby sprawdzic czy dziala

        print("INPUT DZIALA " + input_parameters.preview_option)  # tak zeby sprawdzic czy dziala

        # tutaj beda robione jakies czary z plikiem xD

        file_interpreter = FileInterpreter()
        file_interpreter.interpret_file(request)




        car1 = 'Porsche'

        return redirect(url_for("analyse_data", car=car1))

    else:
        return render_template("spctr_load_data.html")


@app.route("/analyse_data/<car>")
def analyse_data(car):
    # to pokazuje


    print("oł je !")
    print(car)

    return render_template("spctr_results.html")

    # return render_template('form_test.html')
    # wyslij do BE

    # odbierz od BE

    # wyslij na FE


@app.route("/export_results")
def export_results():
    return "Data exported"
