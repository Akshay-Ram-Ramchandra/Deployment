import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify


UPLOAD_FOLDER = '/home/kamla/Desktop/project/Uploaded_Files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def greetings():
    if request.method == 'GET':
        return render_template('uploadpage.html')
@app.route('/upload', methods = ['POST'])
def uploading():
    f = request.files['file']
    f_name = f.filename
    if not f:
        return redirect(url_for('greetings'))
    global save_path
    save_path = os.path.join('/home/kamla/Desktop/project/Uploaded_Files', f_name)
    request.files['file'].save(save_path)
    return redirect(url_for('returning'))

@app.route('/openingcsv', methods = ['GET'])
def returning():
    global a
    a = pd.read_csv(save_path)
    global cols
    cols = a.columns
    data_types = []
    for i in cols:
        data_types.append(a[i].dtypes)
    listolist = []
    for (i, j) in zip(cols, data_types):
        listolist.append([i,j])

    return render_template('return_with_list .html', listolist=listolist)

@app.route('/tgt_select', methods = ['GET'])
def target_select():
    return render_template('Target_selection.html', cols=cols)

@app.route('/display_tgt', methods = ['GET', 'POST'])
def return_tgt():
    global option
    option = request.form['options']
    tgt_dtype = str(a[option].dtype)
    if tgt_dtype == 'float64':
        return render_template('tgt_column_float.html', option=option)
@app.route('/algo', methods = ['GET', 'POST'])
def return_selected():
    option = request.form['options']
    return'Running ' + option


if __name__ == '__main__':
    app.run(debug = True)
