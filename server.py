import torch
import os
from flask import Flask
from flask import request

from database import DatabaseClient

from controllers.file import FileController
from controllers.neural import NeuralNetController 
from neural_net.NeuralNet import Model

# file_controller = FileController('/home/thushima/Documents/git/Monitoramento-de-ambientes-IoT/Raspberry/python/data/collected_data.txt')

FILE_PATH = str(__file__)
MODEL_PATH = FILE_PATH.replace('server.py', 'model')

model = Model(7)
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()

database = DatabaseClient('mongodb+srv://knigth11:knigth11@cluster0.l6ync.mongodb.net/iot?retryWrites=true&w=majority')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, world!'

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        data_json = request.get_json(force=True)
        database.save_data(data_json)
        # file_controller.write_line(data_json)
    return 'saved'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        classes = ['DESLIGA', 'AUMENTA', 'DIMINUI', 'LIGADO' ]

        data_json = request.get_json(force=True)
        # result = neural_controller.predict(data_json)

        data = []

        for key in data_json.keys():
            data.append(float(data_json[key]))

        tensor = torch.tensor(data)
        result = model(tensor).argmax().item()
        return {
            "predicted_action": result,
            "human_action": classes[result] 
        }
    return 'wrong method'

if(__name__ == '__main__'):
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0',debug=False, port=port)