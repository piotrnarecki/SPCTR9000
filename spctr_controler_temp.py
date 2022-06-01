"""

"""

from backend_utils.nlzr import NLZR
from backend_utils.rdr import RDR
from backend_utils.spctr import SPCTR
from frontend_utils.input_parameters import InputParameters

input_parameters = InputParameters(smooth_type = 'SG',
                                   smooth_window_size = 51.0,
                                   range_from = 1450,
                                   range_to = 1750,
                                   smooth_range_type = 'SG',
                                   smooth_range_window_size = 31.0,
                                   baseline_from = 1000,
                                   baseline_to = 2000,
                                   data_normalize_type = 'data_normalize_amide1',
                                   smooth_second_type = 'SG',
                                   smooth_second_window_size = 31.0,
                                   deconvolution_type = 'ble',
                                   bands_value = 'ble')

nlzr = NLZR(input_parameters, RDR, SPCTR)
nlzr.pipeline()
