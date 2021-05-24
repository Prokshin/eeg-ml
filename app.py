import pickle
import sys

import pandas as pd
import sklearn
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def upload_file():
    pkl_Filename = "model.pkl"
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        with open(pkl_Filename, 'rb') as file:
            model = pickle.load(file)
        data = pd.read_csv(uploaded_file, header=None)
        data = pd.DataFrame(data).to_numpy()

        print(len(data[0]), file=sys.stdout)
        res = ''
        if len(data) > 0 and len(data[0]) == 178:
            res = model.predict(data)
        else:
            return 'incorrect data', 400
    return ' '.join(map(str, res))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
