
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_get', methods=['GET'])
def get_prediction():
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))    
    features = [sepal_length, petal_length]
    with open('model.pkl',"rb") as picklefile:
        model = pickle.load(picklefile)
    predicted_class = int(model.predict(features))    
    return jsonify(features=features, predicted_class=predicted_class)

@app.route('/predict_post', methods=['POST'])
def post_predict():
    data = request.get_json(force=True)
    sepal_length = float(data.get('sl'))
    petal_length = float(data.get('pl'))
    
    features = [sepal_length, petal_length]
    with open('model.pkl',"rb") as picklefile:
        model = pickle.load(picklefile)
    predicted_class = int(model.predict(features))
    output = dict(features=features, predicted_class=predicted_class)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
