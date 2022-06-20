from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from frontend_utils.input_parameters import InputParameters
import os
import shutil

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

#klasa odpowiedzalna za zapisanie pliku i skopowanie go do pozniejszej analizy
class FileInterpreter:

    def interpret_file(self, request):
        if request.files['file'].filename != '':

            file = request.files['file']
            file.save(os.path.join(uploads_dir, secure_filename("input_file.csv")))

            filename = file.filename
            print(filename)

            src_path = r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/uploads/input_file.csv"
            dst_path = r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/export_file.csv"
            shutil.copy(src_path, dst_path)
            print('Copied')

            return True
        else:
            return False
            print("NO FILE ")

