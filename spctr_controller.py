from flask import Flask, render_template, abort, request, url_for, flash, redirect, send_file

# ...
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from frontend_utils.input_interpreter import InputInterpreter
from frontend_utils.input_parameters import InputParameters
from frontend_utils.file_interpreter import FileInterpreter
from frontend_utils.chart_utils import ChartUtils
from frontend_utils.download_utils import DownloadUtils


import pandas as pd

from backend_utils.nlzr import NLZR
from backend_utils.rdr import RDR
from backend_utils.spctr import SPCTR
from frontend_utils.input_parameters import InputParameters

from backend_utils.nlzr import NLZR
from backend_utils.rdr import RDR
from backend_utils.spctr import SPCTR

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


app = Flask(__name__)
app.secret_key = "abc"


@app.route("/", methods=['GET', 'POST'])
def get_file():
    if request.method == 'POST':

        file_interpreter = FileInterpreter()
        is_file_correct = file_interpreter.interpret_file(request)

        if (is_file_correct):

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

        input_parameters = input_interpreter.interpret_params(request)

        # obliczenia
        nlzr = NLZR(input_parameters, RDR, SPCTR)
        nlzr.pipeline()

        return redirect(url_for("show_results", preview='p1'))

    else:
        return render_template("get_params.html")


@app.route("/show_results/<preview>")
def show_results(preview):
    chart_utils = ChartUtils()

    main_data = chart_utils.fileToChartData(preview)[0]
    min_data = chart_utils.fileToChartData(preview)[1]

    min_exist =chart_utils.fileToChartData(preview)[2]

    print("PRINT MIN")
    print(min_exist)


    #
    #
    #
    #
    #
    # print("main data")
    # print(main_data)
    #
    #
    #
    #
    #
    #
    # #
    #
    # main_labels = [row[0] for row in main_data]
    # main_values = [row[1] for row in main_data]
    #
    # min_labels = [row[0] for row in min_data]
    # min_values = [row[1] for row in min_data]
    #
    # # heights = [168, 170, 180, 190, 200]
    # # weights = [70, 80, 90, 100, 70]
    # newlist = []
    # for labels, values in zip(main_labels, main_values):
    #     newlist.append({'x': labels, 'y': values})
    # my_data = str(newlist).replace('\'', '')
    #
    # newlist = []
    # for labels, values in zip(min_labels, min_values):
    #     newlist.append({'x': labels, 'y': values})
    # my_data_2 = str(newlist).replace('\'', '')



    # main_labels =  main_data
    # main_values =  main_data
    # min_labels = min_data
    # min_values = min_data


    # return render_template("show_results.html", main_data=main_data  )

    return render_template("show_results.html", main_data=main_data ,min_data=min_data, min_exist=min_exist )


    # return render_template("show_results.html", main_labels=main_labels, main_values=main_values, min_labels=min_labels, min_values=min_values )


@app.route("/export_results/<export_type>", methods=['GET', 'POST'])
def export_results(export_type):
    if request.method == "GET":
        print("EXPORTING")
        # export file

        if (export_type == 'csv'):

            print("EXPORT CSV FILE")

            download_utils = DownloadUtils()
            stream = download_utils.downloadFiles()

            return send_file(
                stream,
                as_attachment=True,
                attachment_filename='spctr9000_results.zip'
            )



        else:

            # dodac metode zapisujaca wyniki
            return "svn exported"

    else:

        return redirect(url_for("show_results", preview='p1'))
