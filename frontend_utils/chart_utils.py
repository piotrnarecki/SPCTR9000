# import pandas as pd
import numpy as np


class ChartUtils:

    # csv zamiast excel

    # def chooseFile(preview):
    #
    #     match preview:
    #         case 'p1':
    #             file_name = 'excel1.xlsx'
    #
    #         case 'p2':
    #             file_name = 'excel2.xlsx'
    #         case 'p3':
    #             file_name = 'excel3.xlsx'
    #
    #     return file_name

    def fileToChartData(self, preview):

        match preview:
            case 'p1':
                file_name = 'csv1.csv'

            case 'p2':
                file_name = 'csv2.csv'

            case 'p3':
                file_name = 'csv3.csv'

            case 'p4':
                file_name = 'csv4.csv'

            case 'p5':
                file_name = 'csv5.csv'

            case 'p6':
                file_name = 'csv6.csv'

            case 'p7':
                file_name = 'csv7.csv'

        path = "/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/csv_files/" + file_name

        data = np.genfromtxt(path, delimiter=';')

        return data
