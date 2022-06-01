"""

"""
import copy
from backend_utils.rdr import RDR
from backend_utils.spctr import SPCTR
from frontend_utils.input_parameters import InputParameters


class NLZR(InputParameters, RDR, SPCTR):
    """
    
    """
    
    def __init__(self,
                 InputParameters: object,
                 RDR: object,
                 SPCTR: object) -> None:
        """
        
        """
        self.input_parameters = InputParameters
        self.rdr: object = RDR()
        self.spctrc: object = SPCTR([])
        self.spctr: object = SPCTR([])
        self.data: list = []
        
        
    def data_provider(self) -> None:
        """
        
        """
        self.rdr.search()
        self.rdr.load()
        self.data = self.rdr.data 
        
        
    def pipeline(self) -> None:
        """
        
        """
        self.data_provider()
        for data in self.data:
            self.spctr.data = data
            self.spctr.save_data('0')
            self.spctrc.data = copy.copy(self.spctr.data)
            
            self.spctrc.smooth(smooth_type = self.input_parameters.smooth_type,
                               smooth_parameter = self.input_parameters.smooth_window_size)
            self.spctrc.save_data('1')
            self.spctrc.cut(cut_type = 'manual',
                            limit_bottom = self.input_parameters.range_from,
                            limit_top = self.input_parameters.range_to)
            self.spctrc.save_data('2')
            self.spctrc.baseline_auto()
            self.spctrc.save_data('3')
            self.spctrc.normalize(normalize_type = self.input_parameters.data_normalize_type)
            self.spctrc.save_data('4')
            self.spctrc.smooth(smooth_type = self.input_parameters.smooth_second_type,
                               smooth_parameter = self.input_parameters.smooth_second_window_size)
            self.spctrc.save_data('5')
            self.spctrc.second_derivative()
            self.spctrc.save_data('6a')
            minimums_index = self.spctrc.find_minimums()
            self.spctrc.save_data('6b')

            self.spctr.smooth(smooth_type = self.input_parameters.smooth_type,
                              smooth_parameter = self.input_parameters.smooth_window_size)
            self.spctr.cut(cut_type = 'manual',
                           limit_bottom = self.input_parameters.range_from,
                           limit_top = self.input_parameters.range_to)
            self.spctr.baseline_auto()
            self.spctr.normalize(normalize_type = self.input_parameters.data_normalize_type)
            self.spctr.smooth(smooth_type = self.input_parameters.smooth_second_type,
                              smooth_parameter = self.input_parameters.smooth_second_window_size)
            self.spctr.save_data('7a')
            self.spctr.spectrum_minimums(minimums_index)
            self.spctr.save_data('7b')
        return
