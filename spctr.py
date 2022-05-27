"""

"""
from BaselineRemoval import BaselineRemoval
from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter
import numpy as np
from scipy.signal import argrelextrema
from scipy.ndimage import rank_filter


class SPCTR():
    """

    """
    
    def __init__(self,
                 data: np.array) -> None:
        """
        
        """
        self.data: np.array = data
        
        
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
                   limit_top: int) -> np.array:
        """
        
        """
        try:
            idx_bottom = (np.abs(self.data[:, 0] - limit_bottom)).argmin()
            idx_top = (np.abs(self.data[:, 0] - limit_top)).argmin()
            self.data = self.data[idx_bottom : idx_top, :]
        except Exception as exc:
            print(exc)
        return
    
    
    def baseline_auto(self) -> None:
        """
        
        """
        POLYNOMINAL_ORDER = 1
        
        try:
            self.data[:, 1] = BaselineRemoval(self.data[:, 1]).ModPoly(POLYNOMINAL_ORDER)
        except Exception as exc:
            print(exc)
        return
    
    #tak racja, można usunąć, auto wystarczy
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
        return
        
    
    def normalize_amide1(self) -> None:
        """
        
        """
        LIMIT_BOTTOM = 1600
        LIMIT_TOP = 1750
        
        idx_bottom = (np.abs(self.data[:, 0] - LIMIT_BOTTOM)).argmin()
        idx_top = (np.abs(self.data[:, 0] - LIMIT_TOP)).argmin()
        print(idx_top)
        max_idx = (np.argmax(self.data[idx_bottom:idx_top + 1, 1]) + idx_bottom)
        print(max_idx)
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

        #plt.figure()
        #plt.plot(self.data[:, 0], self.data[:, 1])
        #plt.title('NORMALIZE AMIDE II')
        #plt.show()

        return
    
    
    def derivative(self):
        """
        
        """
        DERIVATIVE_ORDER = 2
        
        data_spl = UnivariateSpline(self.data[:, 0], self.data[:, 1], s = 0, k = 4)
        self.data[:, 1] = data_spl.derivative(n = DERIVATIVE_ORDER)(self.data[:, 0])
        derivative_2nd = data_spl.derivative(n = DERIVATIVE_ORDER)(self.data[:, 0])
        return derivative_2nd


    def find_local_minimum(self, number):
        """

        """

        local_minimum = argrelextrema(self.data[:, 1], np.less)

        index_local_minimum = local_minimum[0] #wyciagnięcie macierzy
        values_local_minimum = []
        for index in index_local_minimum:
            value = self.data[index, 1]
            if value < 0:
               values_local_minimum.append(value) #wyciągnięcie wartości z indeksu i zapisane ich do nowej listy

        values_local_minimum.sort() #sortowanie wartości, aby funkcja zwracała kilka (number) wybranych wartosci
        values_local_minimum = values_local_minimum[:number]

        return np.array(values_local_minimum)

        
# %%TEST
import matplotlib.pyplot as plt

path = 'C:\\Users\\User\\OneDrive - Politechnika Wroclawska\Pulpit\\SPCTR9000-michal\\input_files\\widmo_z_ATR.csv'


spectrum = np.genfromtxt(path, delimiter = ',')
plt.figure()
plt.plot(spectrum[:, 0], spectrum[:, 1])
plt.title('SPECTRUM')

'''
spctr = SPCTR(spectrum)
spctr.smooth_SG(15)
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('SG FILTER')
'''

'''
spctr = SPCTR(spectrum)
spctr.smooth_FFT(0.0009)
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('FFT FILTER')


spctr = SPCTR(spectrum)
spctr.cut_auto1()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('AUTO CUT AMIDE I & II')

spctr = SPCTR(spectrum)
spctr.cut_auto2()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('AUTO CUT AMIDE I')

spctr = SPCTR(spectrum)
spctr.cut_manual(1000, 2000)
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('MANUAL CUT')

spctr = SPCTR(spectrum)
spctr.smooth_SG(99)
spctr.cut_auto1()
spctr.baseline_auto()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('BASELINE AUTO')

#do wywalenia tak?:
#spctr = SPCTR(spectrum)
#spctr.smooth_SG(99)
#spctr.cut_auto1()
#spctr.baseline_manual(1500, 1700)
#plt.figure()
#plt.plot(spctr.data[:, 0], spctr.data[:, 1])
#plt.title('BASELINE MANUAL')


spctr = SPCTR(spectrum)
spctr.normalize_amide1()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('NORMALIZE AMIDE I')


spctr = SPCTR(spectrum)
spctr.smooth_SG(99)
spctr.cut_auto1()
spctr.baseline_auto()
spctr.normalize_amide2()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.data[:, 1])
plt.title('NORMALIZE AMIDE II')

'''
spctr = SPCTR(spectrum)
spctr.cut_auto1()
spctr.smooth_SG(31)
spctr.baseline_auto()
spctr.normalize_amide1()
plt.figure()
plt.plot(spctr.data[:, 0], spctr.derivative())
plt.title("2'nd DERIVATIVE")
plt.show()

print(spctr.find_local_minimum(5))
