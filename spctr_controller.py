from flask import Flask, render_template, abort, request, url_for, flash, redirect, send_file

# ...
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from frontend_utils.input_interpreter import InputInterpreter
from frontend_utils.input_parameters import InputParameters
from frontend_utils.file_interpreter import FileInterpreter
from frontend_utils.chart_utils import ChartUtils

import pandas as pd

app = Flask(__name__)
app.secret_key = "abc"


# aby zainstalowac panda
# w cmd w folderze projektu:
# pip3 install wheel
# pip3 install pandas
# pip3 install openpyxl


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
            # filename = file_interpreter.get_filename(request)

            return redirect(url_for("get_params"))
        else:
            flash("enter Excel file")
            return render_template("get_file.html")


    else:
        return render_template("get_file.html")
        flash("")


@app.route("/get_params", methods=['GET', 'POST'])
def get_params():
    if request.method == "POST":

        input_interpreter = InputInterpreter()

        # input_parameters - obiekt tej PRZEPIEKNEJ klasy zawiera wszystkie parametry do obliczen
        input_parameters = input_interpreter.interpret_params(request)

        # dziala !
        print("INPUT DZIALA " + input_parameters.deconvolution_type)  # tak zeby sprawdzic czy dziala

        return redirect(url_for("show_results", preview='p1'))

    else:
        return render_template("get_params.html")


@app.route("/show_results/<preview>")
def show_results(preview):
    print("oł je !")
    print(preview)

    chart_utils = ChartUtils()

    data = chart_utils.fileToChartData(preview)

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("show_results.html", labels=labels, values=values)


# return render_template('form_test.html')
# wyslij do BE

# odbierz od BE

# wyslij na FE


@app.route("/export_results/<export_type>", methods=['GET', 'POST'])
def export_results(export_type):
    if request.method == "GET":
        print("EXPORTING")
        # export file

        if (export_type == 'csv'):

            print("EXPORT CSV FILE")

            path=r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/export_file.csv"
            return send_file(path, as_attachment=True)
        else:
            return "svn exported"


            # csv = '1,2,3\n4,5,6\n'
            #
            # # return Response(
            # #     csv,
            # #     mimetype="text/csv",
            # #     headers={"Content-disposition":
            # #                  "attachment; filename=exported_file.csv"})
            #
            # return "Data exported"


        # else:
        #
        #     print("EXPORT JPG FILE")
        #
        #     return redirect(url_for("show_results", preview='p1'))

        # end of export file



    else:

        print("GET XD")
        return redirect(url_for("show_results", preview='p1'))
