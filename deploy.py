from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

print("Current working directory:", os.getcwd())

with open('iris_best_model.pkl', 'rb') as best_model: 
    model = pickle.load(best_model)
with open('lable_encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)


        
