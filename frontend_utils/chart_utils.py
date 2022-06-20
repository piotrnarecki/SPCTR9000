import numpy as np

#klasa odpowiedzialna za zamiane danych z pliku csv z analiza na dane do wykresow
class ChartUtils:

    def fileToChartData(self, preview):

        min_exist=False;

        match preview:
            case 'p1':
                main_file_name = '0.csv'
                min_file_name = '0.csv'

            case 'p2':
                main_file_name = '1.csv'
                min_file_name = '1.csv'
            case 'p3':
                main_file_name = '2.csv'
                min_file_name = '2.csv'
            case 'p4':
                main_file_name = '3.csv'
                min_file_name = '3.csv'
            case 'p5':
                main_file_name = '4.csv'
                min_file_name = '4.csv'
            case 'p6':
                main_file_name = '5.csv'
                min_file_name = '5.csv'
            case 'p7':
                main_file_name = '6a.csv'
                min_file_name = '6b.csv'
                min_exist=True

            case 'p8':
                main_file_name = '7a.csv'
                min_file_name = '7b.csv'
                min_exist=True


        main_path = "/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/" + main_file_name
        min_path = "/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/" + min_file_name

        main_data_list = np.genfromtxt(main_path, delimiter=',')
        min_data_list = np.genfromtxt(min_path, delimiter=',')

        main_labels = [row[0] for row in main_data_list]
        main_values = [row[1] for row in main_data_list]

        min_labels = [row[0] for row in min_data_list]
        min_values = [row[1] for row in min_data_list]


        main_list = []
        for labels, values in zip(main_labels, main_values):
            main_list.append({'x': labels, 'y': values})
        main_data = str(main_list).replace('\'', '')

        min_list = []
        for labels, values in zip(min_labels, min_values):
            min_list.append({'x': labels, 'y': values})
        min_data = str(min_list).replace('\'', '')

        return main_data, min_data, min_exist
