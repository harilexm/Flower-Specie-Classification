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
   - Import `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn` and `pickle`.  

2. **Data Loading & Exploration**  
   - Load `data/iris.csv` into a DataFrame.
   - Inspect `.head()`, `.describe()`. 

3. **Data Preprocessing**  
   - Verify and remove duplicates or missing values.  
   - Encode target labels (`setosa`, `versicolor`, `virginica`) as integers.  
   - Normalize features using `StandardScaler`.  
   - Perform a stratified train/test split (70% train / 30% test).

4. **Model Training & Comparison**  
   - Define candidate classifiers:  
     - Logistic Regression  
     - Support Vector Machine (SVM)  
     - Random Forest  
     - Decision Tree  
   - Fit each model on the training set.  
   - Record cross-validated metrics (accuracy, precision, recall, F1-score).

5. **Evaluation & Selection**  
   - Evaluate each model on the held-out test set:  
     - Overall accuracy  
     - Per-class precision, recall, F1-score  
     - Confusion matrix  
   - Summarize results in a comparison table.  
   - Select the “best” model based on balanced performance.

6. **Artifact Persistence**  
   - Serialize the chosen model to `models/best_model.pkl`.  
   - Serialize the fitted scaler to `models/scaler.pkl`.  

---

### Phase 2 – Web Application (Python Script)

1. **Dependencies**  
   - Ensure `Flask`, `pandas`, `numpy`, and `pickle` are installed (see `requirements.txt`).

2. **App Initialization**  
   - In `app.py`, load `models/best_model.pkl` and `models/scaler.pkl` at startup.  
   - Configure a Flask application with a single `/predict` route.

3. **Input Handling & Prediction**  
   - Render an HTML form (`templates/index.html`) to collect sepal and petal measurements.  
   - On form submission, parse inputs, apply the loaded `StandardScaler`, and call `model.predict_proba()`.  
   - Determine the predicted class and confidence score.

4. **Response Rendering**  
   - Display the predicted species and its probability in a clean, responsive UI.  
   - Serve static assets (CSS, images) from `static/`.

5. **Running the App**  
   ```bash
   python app.py


---

## Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<username>/Flower-Species-Classification.git
   cd Flower-Species-Classification
