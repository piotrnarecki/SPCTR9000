from flask import Flask
from flask import send_file
from glob import glob
from io import BytesIO
from zipfile import ZipFile
import os


class DownloadUtils:

    def downloadFiles(self):

        path = r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/"

        stream = BytesIO()
        with ZipFile(stream, 'w') as zf:
            for file in glob(os.path.join(path, '*.csv')):
                zf.write(file, os.path.basename(file))
        stream.seek(0)

        return stream
