import numpy as np


class ChartUtils:

    def fileToChartData(self, preview):

        deli = ';'
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

            case 'p8':
                file_name = 'export_file.csv'
                deli = ','

        path = "/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/" + file_name

        data = np.genfromtxt(path, delimiter=deli)

        return data
