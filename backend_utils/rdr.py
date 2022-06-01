"""

"""
import os, fnmatch
import numpy as np


class RDR:
    """
    
    """
    
    def __init__(self) -> None:
        """
        
        """
        self.path: str = '.\\imported_files'
        self.extension: str = '*.csv'
        self.files: list = []
        self.data: list = []
    
    
    def search(self) -> tuple:
        """
        
        """
        for root, dirs, files in os.walk(self.path):
            for name in files:
                if fnmatch.fnmatch(name, self.extension):
                    self.files.append([root, name])
        return
    
    
    def load(self) -> None:
        """
        
        """
        for idx, path in enumerate(self.files):
            file = path[0] + '\\' + path[1]
            tmp_data = []
            try:
                if np.shape(np.genfromtxt(file, delimiter = ','))[1] == 2:
                    tmp_data = np.genfromtxt(file, delimiter = ',')
            except:
                try:
                    if np.shape(np.genfromtxt(file, delimiter = ';'))[1] == 2:
                        tmp_data = np.genfromtxt(file, delimiter = ';')
                except:
                    print('ERROR! Uncorrect data format!')
            if tmp_data != list():
                self.data.append(tmp_data)
        return
