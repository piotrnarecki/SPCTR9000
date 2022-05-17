# ta klasa zawiera metody tworzace obiekt z parametrow wejsciowych


from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from frontend_utils.input_parameters import InputParameters


class InputInterpreter:
    # ta piekna funkcja bedzie pobierac dane z wejscia i przerabiac je na obiekt klasy parametry wejsciowe
    def interpret_params(self, request):
        # smooth
        smooth_type = request.form['smooth_radio']
        smooth_window_size = request.form['smooth_window_size']
        # print("smooth: " + smooth_type + " , " + smooth_window_size)

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

        # print("range from " + str(range_from) + " to " + str(range_to))

        # smooth range selected
        smooth_range_type = request.form['smooth_range_radio']
        smooth_range_window_size = request.form['smooth_range_window_size']
        # print("smooth range: " + smooth_range_type + " , " + smooth_range_window_size)

        # baseline

        baseline_type = request.form['baseline_radio']
        baseline_from = 0
        baseline_to = 100
        if baseline_type == "baseline_auto":
            baseline_from = 0
            baseline_to = 100
        else:
            baseline_from = request.form['baseline_from']
            baseline_to = request.form['baseline_to']

        # print("baseline range from " + str(baseline_from) + " ,to " + str(baseline_to))

        # data normalize

        data_normalize_type = request.form['data_normalize_radio']
        # print("data normalize: " + data_normalize_type)

        # smooth second derivative
        smooth_second_type = request.form['smooth_second_radio']
        smooth_second_window_size = request.form['smooth_second_window_size']
        # print("smooth range: " + smooth_second_type + " , " + smooth_second_window_size)

        # deconvolution
        deconvolution_type = request.form['deconvolution_radio']
        # print("deconvolution type: " + deconvolution_type)

        # number of bands
        bands_type = request.form['bands_radio']
        bands_value = 1
        if bands_type == "bands_number":
            bands_value = request.form['number_value']

        else:
            bands_value = request.form['treshold_value']
        # print("bands type" + bands_type + " value: " + str(bands_value))

        preview_option = request.form['preview_option']
        # print("preview option: " + preview_option)

        export_option = request.form['export_radio']
        # print("export option: " + export_option)

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
                                           deconvolution_type,
                                           bands_type,
                                           bands_value,
                                           preview_option,
                                           export_option
                                           )

        return input_parameters

    def interpret_file(self, request):
        print("file interpreter TEST")
