import pickle
import sklearn


def jayden(inputs):
    model = pickle.load(open('Model.pkl', 'rb'))
    return model.predict([inputs])[0]


def taylor(inputs):
    model = pickle.load(open('baseline_model2.pkl', 'rb'))
    return model.predict([inputs])[0]
