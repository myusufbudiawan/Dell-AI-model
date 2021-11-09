import os

from flask import Flask, render_template, request, jsonify
from flask_dropzone import Dropzone
import requests
import pandas as pd

# variable declare
basedir = os.path.abspath(os.path.dirname(__file__))

dataset_path = ""

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

        data = pd.read_csv(file_path, encoding='latin-1')

        data.to_csv(target_csv_path, index=False)

        print("Download ready.")

    return render_template('index.html')


@app.route('/finish')
def process():

    from Website import process, attr_retrieval

    print(attr_retrieval.dataset_size())
    print(attr_retrieval.is_supervise())
    print(attr_retrieval.is_binary())
    print(attr_retrieval.det_goal())

    process.process_data()

    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
