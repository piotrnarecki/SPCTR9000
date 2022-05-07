# ta klasa zawiera metody tworzace obiekt z parametrow wejsciowych


from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


class InputInterpreter:
    # ta piekna funkcja bedzie pobierac dane z wejscia i przerabiac je na obiekt klasy parametry wejsciowe
    def interpret_params(self, request):
        # smooth
        smooth_type = request.form['smooth_radio']
        smooth_window_size = request.form['smooth_window_size']
        print("smooth: " + smooth_type + " , " + smooth_window_size)

        # range
        range_type = request.form['range_radio']
        range_from = 0
        range_to = 1

        match range_type:
            case "range_1":
                range_from = 1
                range_to = 10
            case "range_2":
                range_from = 5
                range_to = 15
            case "custom_range":
                range_from = request.form['range_from']
                range_to = request.form['range_to']

        print("range from: " + str(range_from) + " to: " + str(range_to))

        # smooth range selected




        # baseline
        # data normalize
        # smooth second derivative
        # deconvolution
        # number of bands

    def interpret_file(self, request):
        print("file interpreter TEST")
