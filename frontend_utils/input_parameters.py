class InputParameters:

    def __init__(self,
                 smooth_type,
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
                 # deconvolution_type,
                 bands_value
                 # preview_option,
                 # export_option

                 ):
        self.smooth_type = smooth_type
        self.smooth_window_size = smooth_window_size
        self.range_from = range_from
        self.range_to = range_to
        self.smooth_range_type = smooth_range_type
        self.smooth_range_window_size = smooth_range_window_size
        self.baseline_from = baseline_from
        self.baseline_to = baseline_to
        self.data_normalize_type = data_normalize_type
        self.smooth_second_type = smooth_second_type
        self.smooth_second_window_size = smooth_second_window_size
        # self.deconvolution_type = deconvolution_type
        self.bands_value = bands_value
        # self.preview_option = preview_option
        # self.export_option = export_option
