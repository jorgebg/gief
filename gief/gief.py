import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return '''
    <!doctype html>
    <title>Gimme</title>
    <h1>Gimme</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/', methods=['POST'])
def post():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['path'], filename))
    return filename + ' uploaded'
