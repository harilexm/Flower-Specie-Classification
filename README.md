# Flower-Species-Classification

Predict the species of an Iris flower Setosa, Versicolor or Virginica by using an end-to-end machine learning pipeline and deploy the best model in a web app.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [Pipeline & Model Workflow](#pipeline--model-workflow)  
4. [Installation & Usage](#installation--usage)  
5. [Results](#results)  
6. [Project Structure](#project-structure)  
7. [Future Work](#future-work)  

---

## Project Overview

This repository implements a complete workflow for multiclass classification on the classic Iris dataset. It covers:

- Data gathering & Loading in Editor  
- Preprocessing (cleaning, scaling, train/test split)  
- Training and comparing multiple classifiers  
- Selecting and persisting the best model
- Creat8hg a Flask WebApp & deploying the best model
- Getting predictions through a Flask web-interface  

---

## Dataset

- **Source:** Kaggle Iris dataset (150 samples, 4 features)  
- **Classes:**  
  - *Iris-setosa*  
  - *Iris-versicolor*  
  - *Iris-virginica*  
- **Features:** sepal length, sepal width, petal length, petal width  

---

## Pipeline & Model Workflow

### Phase 1 – Preprocessing & Modeling (Jupyter Notebook)

1. **Environment & Libraries**  
   - Load necessary Libraries.  

2. **Data Loading & Exploration**  
   - Load dataset & Understand it.

3. **Data Preprocessing**  
   - Preprocess data by removing dublicates or missing values, encode the labels, normalize the features & split data into 30-70% ratio.

4. **Model Training & Comparison**  
   - Experience & Train different models as  
     - Logistic Regression  
     - Support Vector Machine (SVM)  
     - Random Forest  
     - Decision Tree
     - Naive Bayes

5. **Evaluation & Selection**  
   - Evaluate each model on the test set.  
   - Select the “best” model based on balanced performance.

6. **Artifact Persistence**  
   - Save the best model as  `iris_best_model.pkl`.  
   - Save the LabelEncoder as `label_encoder.pkl` & StandardScaler as `scalar.pkl`.  

---

### Phase 2 – Web Application (Python Script)

1. **Dependencies**  
   - Ensure `Flask`, `pandas`, `numpy`, and `pickle` are installed.

2. **App Initialization**  
   - Load `best_model.pkl` `label_encoder.pkl`and `scaler.pkl` at startup.

3. **Input Handling & Prediction**  
   - From (`templates/index.html`) to collect sepal and petal measurements.  
   - On form submission, parse inputs, apply the loaded `label_encoder` & `StandardScaler`, and call `model.predict_proba()`.  
   - Determine the predicted class and confidence score.

4. **Response Rendering**  
   - Displaying the predicted species and its probability in UI.

---

## Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<username>/Flower-Species-Classification.git
   cd Flower-Species-Classification
