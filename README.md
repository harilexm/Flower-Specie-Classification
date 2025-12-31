# Flower Species Classification

Predict the species of an Iris flower Setosa, Versicolor or Virginica by using an end-to-end machine learning pipeline and deploy the best model in a web app for user testing.
<p align="center">
  <img src="assets/image.png" alt="Project Demo" width="800"/>
</p>

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset](#dataset)  
3. [System Overview](#System-Overview)  
4. [Installation & Usage](#installation--usage)
5. [Results](#results)  

---

## Project Overview

This repository implements a complete workflow for multiclass classification on the classic Iris dataset. It covers:

- Data gathering & Loading in Editor  
- Preprocessing (cleaning, encoding, scaling, train/test split)  
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

## System Overview

### Phase 1 – Preprocessing & Modeling (Jupyter Notebook)

1. **Environment & Libraries**
2. **Data Loading & Exploration**
3. **Data Preprocessing**
4. **Model Training & Comparison**  
5. **Evaluation & Selection**  
6. **Saving Model, Encoder & Scalar as .pkl**
   
---

### Phase 2 – Web Application (Python Script)

1. **Dependencies**
2. **App Initialization**  
3. **Input Handling & Prediction**  
4. **Response Rendering**  
   
---

## Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<username>/Flower-Species-Classification.git
   cd Flower-Species-Classification

---

## Results

These are results of the Five Algorithms used:
1. 95.19% : Logistic Regression
2. 95.14% : Decision Tree
3. 96.710% : Random Forest
4. 97.10% : SVM
5. 95.14% : Naive Bayes

The Choosen Best model is SVM with an accuracy of 97.10%.
