# Project Title: Amazon Product Review Sentiment Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Training and Evaluation](#model-training-and-evaluation)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

### Introduction

This project aims to analyze the sentiment of Amazon product reviews using various machine learning models. The dataset consists of product reviews labeled as positive or negative. The project involves data preprocessing, feature extraction using TF-IDF, and training multiple machine learning models to classify the reviews.

### Dataset

The dataset used in this project consists of Amazon product reviews with labels indicating whether they are positive or negative. The dataset is split into training and testing sets.

*   **Train Dataset:** Contains the reviews used to train the models.
*   **Test Dataset:** Contains the reviews used to evaluate the models.

### Installation

To run this project, you need to have the following libraries installed:

```bash
pip install pandas scikit-learn nltk joblib matplotlib seaborn wordcloud xgboost catboost scikit-optimize
```

### Usage

1.  **Mount Google Drive and Load Data:** The dataset is loaded from Google Drive.
2.  **Data Preprocessing:** The text data is cleaned, lemmatized, and combined.
3.  **Feature Engineering:** TF-IDF is used to extract features from the text data.
4.  **Model Training and Evaluation:** Various machine learning models are trained and evaluated.

### Model Training and Evaluation

The following models are trained and evaluated in this project:

1.  Logistic Regression
2.  Support Vector Machine (SVM)
3.  Random Forest
4.  Gradient Boosting
5.  AdaBoost
6.  Extra Trees
7.  XGBoost
8.  CatBoost
9.  Multinomial Naive Bayes
10. Voting Classifier (Ensemble Model)

### Results

The performance of each model is evaluated using precision, recall, and F1-score. The best-performing model is selected based on these metrics. 
| Model                       | Accuracy | Precision | Recall | F1-Score |
|-----------------------------|----------|-----------|--------|----------|
| Logistic Regression         | 85%      | 0.85      | 0.85   | 0.85     |
| SVM                         | 86%      | 0.86      | 0.86   | 0.86     |
| Random Forest               | 83%      | 0.83      | 0.83   | 0.83     |
| Gradient Boosting           | 79%      | 0.79      | 0.79   | 0.79     |
| AdaBoost                    | 81%      | 0.81      | 0.81   | 0.81     |
| Extra Trees                 | 84%      | 0.84      | 0.84   | 0.84     |
| XGBoost                     | 82%      | 0.82      | 0.82   | 0.82     |
| CatBoost                    | 82%      | 0.82      | 0.82   | 0.82     |
| Multinomial Naive Bayes     | 83%      | 0.83      | 0.83   | 0.83     |
| Voting Classifier (Ensemble)| 84%      | 0.84      | 0.84   | 0.84     |




### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License
This project is licensed under the MIT License.
