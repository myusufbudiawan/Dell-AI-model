import os

from flask import Flask, render_template, request, jsonify
from flask_dropzone import Dropzone
from pandas.core.frame import DataFrame
import requests
import pandas as pd

# variable declare
basedir = os.path.abspath(os.path.dirname(__file__))

dataset_path = ""
result = "null"

app = Flask(__name__)

target_csv_path = "input.csv"

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_MAX_FILE_SIZE=300,
    DROPZONE_MAX_FILES=1,
    # allow only excel file(xlsx)
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='.csv'
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)

        f.save(file_path)

        data = pd.read_csv(file_path)

        data.to_csv(target_csv_path, index=False)

        print("Download ready.")

    return render_template('index.html')


@app.route('/result')
def process():

    from Website import process, attr_retrieval

    ds_size = attr_retrieval.dataset_size()
    #is_supervised = attr_retrieval.is_supervise()
    is_binary = attr_retrieval.is_binary()
    print(is_binary)
    ds_goal = attr_retrieval.det_goal()

    predict_df = [[is_binary, ds_goal, ds_size, 'null']]

    display_df = ["is binary: " + is_binary, "dataset goal: " +
                  ds_goal, "dataset size: " + ds_size]

    result = process.process_data(predict_df)

    print(result)

    return render_template('result.html', value=result, displayDf=display_df)


if __name__ == '__main__':
    app.run(debug=True)
