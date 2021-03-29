from neural_net.NeuralNet import Model

def load_model(model_path):
    model = None
    try:
        model = Model(7)
        model.load_state_dict(model_path)
        model.eval()
    except Exception as e:
        print(e)
    finally:
        return model
    