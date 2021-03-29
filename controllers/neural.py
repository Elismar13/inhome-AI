import torch
import torch.nn as nn
import torch.nn.functional as F

from neural_net.load_model import load_model

class NeuralNetController():
    def __init__(self, model_path: str):
        self.model = load_model(model_path)

    def predict(self, data):
        try:
            input_data = self.parse_input(data)
            input_predict = torch.tensor(input_data)
            predict = self.model.forward(input_predict)

            return predict.argmax().item()
        except Exception as e:
            print(e)
            return 'Error'

    def parse_input(self, input_dict):
        input_predict_data = []

        for key in input_dict.keys():
            input_predict_data.append(float(input_dict[key]))

        return input_predict_data
        