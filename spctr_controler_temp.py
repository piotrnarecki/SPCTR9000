"""

"""

from backend_utils.nlzr import NLZR
from backend_utils.rdr import RDR
from backend_utils.spctr import SPCTR
from frontend_utils.input_parameters import InputParameters


nlzr = NLZR(InputParameters, RDR, SPCTR)
nlzr.pipeline()
