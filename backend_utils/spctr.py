"""

"""
from BaselineRemoval import BaselineRemoval
from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import numpy as np


class SPCTR():
    """
    
    """
    
    def __init__(self,
                 data: np.array) -> None:
        """
        
        """
        self.data: np.array = data
        
    
    def plot_data(self,
                  title: str) -> None:
        """
        
        """
        plt.figure()
        plt.plot(self.data[:, 0], self.data[:, 1], '.', markersize = 2)
        plt.title(title)
        return
    
    
    def smooth_SG(self,
                  window_length: int) -> None:
        """
        
        """
        POLYNOMINAL_ORDER = 2
        
        try:
            if (
                    window_length > 2
                    ):
                self.data[:, 1] = savgol_filter(self.data[:, 1], window_length, POLYNOMINAL_ORDER)
        except Exception as exc:
            print(exc)
        return
    
    
    def smooth_FFT(self,
                   threshold: float) -> None:
        """
        
        """
        try:
            signal = self.data[:, 1]
            sample_number = len(self.data[:, 0])
            
            signal_fft = np.fft.fft(signal, sample_number)
            PSD = signal_fft * np.conj(signal_fft) / sample_number
            
            indices = PSD > threshold
            signal_ifft = np.fft.ifft(indices * signal_fft)
            
            self.data[:, 1] = signal_ifft
        except Exception as exc:
            print(exc)
        return
    
    
    def smooth(self,
               smooth_type: str,
               smooth_parameter: float) -> None:
        """
        
        """
        if smooth_type == 'SG':
            self.smooth_SG(int(smooth_parameter))
        elif smooth_type == 'FFT':
            self.smooth_FFT(smooth_parameter)
        else:
            print('ERROR! Incorrect smoothing type!')
        return
    
    
    def cut_auto1(self) -> None:
        """
        
        """
        LIMIT_BOTTOM = 1450
        LIMIT_TOP = 1750
        
        try:
            idx_bottom = (np.abs(self.data[:, 0] - LIMIT_BOTTOM)).argmin()
            idx_top = (np.abs(self.data[:, 0] - LIMIT_TOP)).argmin()
            self.data = self.data[idx_bottom : idx_top, :]
        except Exception as exc:
            print(exc)
        return
    
    
    def cut_auto2(self) -> None:
        """
        
        """
        LIMIT_BOTTOM = 1600
        LIMIT_TOP = 1750
        
        try:
            idx_bottom = (np.abs(self.data[:, 0] - LIMIT_BOTTOM)).argmin()
            idx_top = (np.abs(self.data[:, 0] - LIMIT_TOP)).argmin()
            self.data = self.data[idx_bottom : idx_top, :]
        except Exception as exc:
            print(exc)
        return
    
    
    def cut_manual(self,
                   limit_bottom: int,
                   limit_top: int) -> None:
        """
        
        """
        try:
            idx_bottom = (np.abs(self.data[:, 0] - limit_bottom)).argmin()
            idx_top = (np.abs(self.data[:, 0] - limit_top)).argmin()
            self.data = self.data[idx_bottom : idx_top, :]
        except Exception as exc:
            print(exc)
        return
    
    
    def cut(self,
            cut_type: str,
            limit_bottom: int,
            limit_top: int) -> None:
        """
        
        """
        if cut_type == 'auto1':
            self.cut_auto1()
        elif cut_type == 'auto2':
            self.cut_auto2()
        elif cut_type == 'manual':
            self.cut_manual(limit_bottom, limit_top)
        else:
            print('ERROR! Incorrect cutting type!')
        return
    
    
    def baseline_auto(self) -> None:
        """
        
        """
        POLYNOMINAL_ORDER = 1
        
        try:
            self.data[:, 1] = BaselineRemoval(self.data[:, 1]).ModPoly(POLYNOMINAL_ORDER)
            minimums_index = argrelextrema(self.data[:, 1], np.less)[0]
            self.data = self.data[minimums_index[0]:minimums_index[-1], :]
        except Exception as exc:
            print(exc)
        return
    
    
    def baseline_manual(self,
                        min_a: int,
                        min_b: int) -> None:
        """
        
        """        
        try:
            idx_a = (np.abs(self.data[:, 0] - min_a)).argmin()
            idx_b = (np.abs(self.data[:, 0] - min_b)).argmin()
            y_a = self.data[idx_a, 1]
            y_b = self.data[idx_b, 1]
            x_a = self.data[idx_a, 0]
            x_b = self.data[idx_b, 0]
            m = (y_b - y_a) / (x_b - x_a)
            c = y_a - m * x_a
            self.data[:, 1] = self.data[:, 1] - (self.data[:, 0] * m + c)
            #self.data[:, 1][self.data[:, 1] < 0] = 0
        except Exception as exc:
            print(exc)
        self.plot_data('BASELINE MANUAL')
        return
        
    
    def normalize_amide1(self) -> None:
        """
        
        """
        LIMIT_BOTTOM = 1600
        LIMIT_TOP = 1750
        
        idx_bottom = (np.abs(self.data[:, 0] - LIMIT_BOTTOM)).argmin()
        idx_top = (np.abs(self.data[:, 0] - LIMIT_TOP)).argmin()
        max_idx = (np.argmax(self.data[idx_bottom:idx_top + 1, 1]) + idx_bottom)
        self.data[:, 1] = self.data[:, 1] / self.data[max_idx, 1]
        return
        
    
    def normalize_amide2(self) -> None:
        """
        
        """
        LIMIT_BOTTOM = 1450
        LIMIT_TOP = 1600
        
        idx_bottom = (np.abs(self.data[:, 0] - LIMIT_BOTTOM)).argmin()
        idx_top = (np.abs(self.data[:, 0] - LIMIT_TOP)).argmin()
        max_idx = (np.argmax(self.data[idx_bottom:idx_top + 1, 1]) + idx_bottom)
        self.data[:, 1] = self.data[:, 1] / self.data[max_idx, 1]
        return
    
    
    def normalize(self,
                  normalize_type: str) -> None:
        if normalize_type == 'data_normalize_none':
            pass
        elif normalize_type == 'data_normalize_amide1':
            self.normalize_amide1()
        elif normalize_type == 'data_normalize_amide2':
            self.normalize_amide2()
        else:
            print('ERROR! Incorrect normalization type!')
        return
    
    
    def second_derivative(self) -> None:
        """
        
        """
        DERIVATIVE_ORDER = 2
        
        data_spl = UnivariateSpline(self.data[:, 0], self.data[:, 1], s = 0, k = 4)
        self.data[:, 1] = data_spl.derivative(n = DERIVATIVE_ORDER)(self.data[:, 0])
        return
    
    
    def find_minimums(self) -> np.array:
        """
        
        """
        WINDOW_LENGTH = 21
        
        self.smooth_SG(WINDOW_LENGTH)
        minimums_index = argrelextrema(self.data[:, 1], np.less)[0]
        self.data = self.data[minimums_index]
        #self.plot_data('MINIMUMS')
        #plt.plot(minimums[:, 0], minimums[:, 1], '.')
        return minimums_index
    
    
    def spectrum_minimums(self, minimums_index):
        """
        
        """
        WINDOW_LENGTH = 21
        
        self.smooth_SG(WINDOW_LENGTH)
        self.data = self.data[minimums_index]
        #self.plot_data('PEAKS')
        #x_axis = self.data[:, 0][minimums_index]
        #y_axis = self.data[:, 1][minimums_index]
        #plt.plot(x_axis, y_axis, '.')
        #for idx, txt in enumerate(x_axis):
        #    plt.annotate(round(txt), (x_axis[idx], y_axis[idx]))
        return
        
        
    def save_data(self,
                  name: str) -> None:
        """
        
        """
        np.savetxt(('.\\exported_files\\' + name + '.csv'), self.data, delimiter = ',', fmt='%f')
        return
