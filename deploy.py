from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

print("Current working directory:", os.getcwd())

with open('iris_best_model.pkl', 'rb') as model_file: 
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # user input data
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    
    features = [[sepal_length, sepal_width, petal_length, petal_width]] # feature array
    features = scaler.transform(features)                               # Preprocess
    prediction = model.predict(features)                                # Make prediction
    probabilities = model.predict_proba(features)                       # Get probabilities
    
    # Get the probability of the predicted class
    confidence = round(max(probabilities[0]) * 100, 2)
    
    return render_template('result.html', prediction=prediction[0], accuracy=f"{confidence}%")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)