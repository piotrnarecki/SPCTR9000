from flask import Flask, render_template, abort, request, url_for, flash, redirect

# ...
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from frontend_utils.input_interpreter import InputInterpreter
from frontend_utils.input_parameters import InputParameters
from frontend_utils.file_interpreter import FileInterpreter

app = Flask(__name__)


# WPISZ PONISZE KOMENTY W TERMINAL NA DOLE ABY URUCHOMIC
# export FLASK_APP=spctr9000_controller.py
# export FLASK_ENV=developer
# export FLASK_DEBUG=1
# flask run


@app.route("/", methods=['GET', 'POST'])
def get_file():
    if request.method == 'POST':

        # tutaj beda robione jakies czary z plikiem xD

        file_interpreter = FileInterpreter()
        is_file_correct = file_interpreter.interpret_file(request)

        if (is_file_correct):
            return redirect(url_for("get_params"))
        else:
            return "WRONG !"


    else:
        return render_template("get_file.html")


@app.route("/get_params", methods=['GET', 'POST'])
def get_params():
    if request.method == "POST":

        input_interpreter = InputInterpreter()

        # input_parameters - obiekt tej PRZEPIEKNEJ klasy zawiera wszystkie parametry do obliczen
        input_parameters = input_interpreter.interpret_params(request)

        # dziala !
        print("INPUT DZIALA " + input_parameters.deconvolution_type)  # tak zeby sprawdzic czy dziala

        # print("INPUT DZIALA " + input_parameters.preview_option)  # tak zeby sprawdzic czy dziala

        car1 = 'Porsche'

        return redirect(url_for("show_results", car=car1))

    else:
        return render_template("get_params.html")


@app.route("/show_results/<car>")
def show_results(car):
    # to pokazuje

    print("oł je !")
    print(car)

    data = [

        (200, 120),
        (300, 150),
        (400, 140.32),
        (500, 180.45),
        (600, 200.5),
        (700, 220),
        (800, 170),

    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("show_results.html", labels=labels, values=values)


# return render_template('form_test.html')
# wyslij do BE

# odbierz od BE

# wyslij na FE


@app.route("/export_results")
def export_results():
    return "Data exported"
