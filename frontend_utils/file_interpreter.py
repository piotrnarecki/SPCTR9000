from flask import Flask, render_template, abort, request, url_for, flash, redirect

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from frontend_utils.input_parameters import InputParameters
import os



class FileInterpreter:
    # ta piekna funkcja bedzie pobierac plik
    def interpret_file(self, request):
        if request.files['file'].filename != '':
            file = request.files['file']
            file.save(secure_filename(file.filename))
            # file.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
            # file.save(os.path.join(app.root_path, 'input_files', secure_filename(file.filename)))

            print(file.filename)
            # return 'file uploaded successfully'
            return True
        else:
            return False
            print("NO FILE ")
            # return redirect(url_for("load_data"))
