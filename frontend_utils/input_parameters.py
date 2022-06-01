class InputParameters:

    def __init__(self):
        self.smooth_first_type: str = 'SG'
        self.smooth_first_parameter: float = 51.0
        self.cut_type: str = 'auto1'
        self.cut_limit_bottom: int = 1000
        self.cut_limit_top: int = 2000
        self.baseline_type: str = 'auto'
        self.normalize_type: str = 'amide2' #'data_normalize_none' / 'data_normalize_amide1' / 'data_normalize_amide2'
        self.smooth_second_type: str = 'SG'
        self.smooth_second_parameter: float = 31.0
        self.preview_option: str = 'preview'
        self.export_option: str = 'export'





