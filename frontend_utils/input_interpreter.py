from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from frontend_utils.input_parameters import InputParameters

#klasa odpowiedzialana za odczytanie z requestu parametrow analizy
class InputInterpreter:
    def interpret_params(self, request):

        smooth_type = request.form['smooth_radio']
        smooth_window_size = request.form['smooth_window_size']

        range_type = request.form['range_radio']
        range_from = 0
        range_to = 1

        match range_type:
            case "range_1":
                range_from = 1490
                range_to = 1750
            case "range_2":
                range_from = 1590
                range_to = 1750
            case "custom_range":
                range_from = request.form['range_from']
                range_to = request.form['range_to']

        smooth_range_type = request.form['smooth_range_radio']
        smooth_range_window_size = request.form['smooth_range_window_size']

        baseline_type = request.form['baseline_radio']
        baseline_from = 0
        baseline_to = 100

        if baseline_type == "baseline_auto":
            baseline_from = 0
            baseline_to = 100
        else:
            baseline_from = request.form['baseline_from']
            baseline_to = request.form['baseline_to']

        data_normalize_type = request.form['data_normalize_radio']

        smooth_second_type = request.form['smooth_second_radio']
        smooth_second_window_size = request.form['smooth_second_window_size']

        bands_value = request.form['number_value']

        input_parameters = InputParameters(smooth_type,
                                           smooth_window_size,
                                           range_from,
                                           range_to,
                                           smooth_range_type,
                                           smooth_range_window_size,
                                           baseline_from,
                                           baseline_to,
                                           data_normalize_type,
                                           smooth_second_type,
                                           smooth_second_window_size,
                                           bands_value
                                           )

        return input_parameters


