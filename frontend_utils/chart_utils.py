import pandas as pd


class ChartUtils:

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
                file_name = 'excel1.xlsx'
                data = [
                    (200, 20),
                    (300, 50),
                    (400, 40.32),
                    (500, 80.45),
                    (600, 100.5),
                    (700, 120),
                    (800, 70),
                    (900, 120),
                    (1000, 270)
                ]

            case 'p2':
                file_name = 'excel2.xlsx'
                data = [
                    (200, 120),
                    (300, 150),
                    (400, 140.32),
                    (500, 180.45),
                    (600, 200.5),
                    (700, 220),
                    (800, 170),
                    (900, 220),
                    (1000, 170)
                ]
            case 'p3':
                file_name = 'excel3.xlsx'
                data = [

                    (400, 410.32),
                    (500, 380.45),
                    (600, 500.5),
                    (700, 520),
                    (800, 470),
                    (900, 400),
                    (1000, 540)
                ]

        # file_name = chooseFile(preview)

        file_path = r'excel_files/' + file_name

        df = pd.read_excel(
            file_path)  # place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'

        print(df)
        # mylist = df['A1:A20'].tolist()

        return data
