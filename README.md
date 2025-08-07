# Flower-Species-Classification

Predict the species of an Iris flower—Setosa, Versicolor, or Virginica—using an end-to-end machine learning pipeline and deploy the best model in a web app.

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

- Data ingestion and exploratory analysis  
- Preprocessing (cleaning, scaling, train/test split)  
- Training and comparing multiple classifiers  
- Selecting and persisting the best model  
- Deploying predictions through a Flask web interface  

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

1. **Libraries**  
   - pandas, NumPy, scikit-learn, Flask, pickle  
2. **Load & Explore**  
   - Read `iris.csv`; inspect summary statistics and class balance  
3. **Preprocessing**  
   - Handle duplicates/missing values (if any)  
   - Standardize features with `StandardScaler`  
   - Stratified train/test split (70% train, 30% test)  
4. **Model Selection**  
   Train and evaluate four algorithms on the test set:  
   - Logistic Regression  
   - Support Vector Machine (SVM)  
   - Random Forest  
   - Decision Tree  
5. **Evaluation Metrics**  
   - Accuracy, precision, recall, F1-score  
   - Confusion matrix  
6. **Best Model**  
   - Select by highest test accuracy and balance of precision/recall  
7. **Persistence**  
   - Serialize chosen model and scaler to `models/` with `pickle`  
8. **Web Deployment**  
   - Flask app accepts user inputs, returns species prediction and confidence  

---

## Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<username>/Flower-Species-Classification.git
   cd Flower-Species-Classification
