from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from frontend_utils.input_parameters import InputParameters
import os
import shutil

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

class FileInterpreter:
    # ta piekna funkcja bedzie pobierac plik


    def interpret_file(self, request):
        if request.files['file'].filename != '':
            # file = request.files['file']
            # file.save(secure_filename(file.filename))
            # file.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
            # file.save(os.path.join(app.root_path, 'input_files', secure_filename(file.filename)))




            # save the single "profile" file
            file = request.files['file']
            file.save(os.path.join(uploads_dir, secure_filename("input_file.csv")))

            filename = file.filename
            print(filename)

            # kopiuje do drugiego folderu
            src_path = r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/uploads/input_file.csv"
            dst_path = r"/Volumes/SD/Projects/PycharmProjects/pythonProject/SPCTR9000/instance/export/export_file.csv"
            shutil.copy(src_path, dst_path)
            print('Copied')



            # return 'file uploaded successfully'
            return True
        else:
            return False
            print("NO FILE ")
            # return redirect(url_for("load_data"))

    def get_filename(self,request):
        if request.files['file'].filename != '':
            file = request.files['file']
            filename = file.filename
            return filename
        else:
            return ""