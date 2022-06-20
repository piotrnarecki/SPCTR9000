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



# metoda otwierajaca okno strony glownej
# jesli uzytkownik wybierze plik do analizy to zostanie on wczytany a okno z wyborem parametrów zostanie otwarte
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

# metoda pobierajaca od uzytkownika parametry analizy
# po wybraniu parametrow zaczyna sie analiza
@app.route("/get_params", methods=['GET', 'POST'])
def get_params():
    if request.method == "POST":

        #instancja obiektu klasy odpowiedzialnej za przetwarzanie wejscia z UI
        input_interpreter = InputInterpreter()

        #instancja obiektu klasy odpowiedzialnej za przekazywanie parametrow wejsciowych na backend
        input_parameters = input_interpreter.interpret_params(request)

        # instancja obiektu klasy odpowiedzialnej za analize danych
        nlzr = NLZR(input_parameters, RDR, SPCTR)
        nlzr.pipeline()

        #przekierowanie na okno z wynikami analizy
        return redirect(url_for("show_results", preview='p1'))

    else:
        return render_template("get_params.html")

# metoda wyswietlajaca wyniki analizy
@app.route("/show_results/<preview>")
def show_results(preview):
    chart_utils = ChartUtils()

    main_data = chart_utils.fileToChartData(preview)[0]
    min_data = chart_utils.fileToChartData(preview)[1]

    min_exist =chart_utils.fileToChartData(preview)[2]

    #przekazywanie danych z backendu na frontend
    return render_template("show_results.html", main_data=main_data ,min_data=min_data, min_exist=min_exist )


# metoda odpowiedzialna za eksport danych
@app.route("/export_results/<export_type>", methods=['GET', 'POST'])
def export_results(export_type):
    if request.method == "GET":


        print("EXPORT CSV FILE")

        download_utils = DownloadUtils()
        stream = download_utils.downloadFiles()

        #eksport wynikow w postaci zipa z plikami csv
        return send_file(
            stream,
            as_attachment=True,
            attachment_filename='spctr9000_results.zip'
        )


    else:

        return redirect(url_for("show_results", preview='p1'))
