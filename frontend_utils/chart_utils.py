import numpy as np


class ChartUtils:

    def fileToChartData(self, preview):


        match preview:
            case 'p1':
                file_name = '0.csv'

            case 'p2':
                file_name = '1.csv'

            case 'p3':
                file_name = '2.csv'

            case 'p4':
                file_name = '3.csv'

            case 'p5':
                file_name = '4.csv'

            case 'p6':
                file_name = '5.csv'

            case 'p7':
                file_name = '6a.csv'

            case 'p8':
                file_name = '7a.csv'


        path = "/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/" + file_name

        data = np.genfromtxt(path, delimiter=',')

        return data
