from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

print("Current working directory:", os.getcwd())

with open('iris_best_model.pkl', 'rb') as best_model: 
    model = pickle.load(best_model)
with open('label_encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    probabilities = None

    if request.method == "POST":
        try:
            features = [float(request.form["f1"]), float(request.form["f2"]), request.form(["f3"]), float(request.form["f4"])]
            X = np.array(features).shape(1, -1)

            probs = model.predict_proba(X)[0]
            class_index = np.argmax(probs)

            prediction = encoder.inverse_transform([class_index])[0]
            confidence = round(probs[class_index] * 100, 2)
            probabilities = dict(zip(encoder.classes_, (probs * 100).round(2)))
        except Exception as e:
            print("prediction error:", e)

        
    return render_template("index.html", prediction = prediction, confidence = confidence, probabilities = probabilities)
    
if __name__ == "__main__":
    app.run(debug = True)