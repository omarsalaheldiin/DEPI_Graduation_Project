# Sentiment Analysis Experiment Tracking with MLflow

## Introduction

This section showcases the use of MLflow for tracking and managing machine learning experiments. MLflow's main features utilized in this project include experiments, runs, artifacts, logging metrics and parameters, and model registering. The code handles training and evaluating ten different models, registering the top five based on their evaluation scores.

## MLflow Features

- **Experiments:** Organize runs under a single project.
- **Runs:** Capture and record data about individual model training sessions.
- **Artifacts:** Store outputs like confusion matrix heatmaps.
- **Logging Metrics and Parameters:** Track model performance and hyperparameters.
- **Model Registering:** Save the best models for later use or deployment.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - mlflow
  - scikit-learn
  - matplotlib
  - seaborn
  - pyngrok

## Code Breakdown

### Setting Up the Experiment

```python
mlflow.set_experiment("sentiment_analysis_experiment")
```

### Models Tracking

The code evaluates ten models:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Random Forest
4. Gradient Boosting
5. AdaBoost
6. Extra Trees
7. XGBoost
8. CatBoost
9. Multinomial Naive Bayes
10. Voting Classifier (Ensemble Model)

MLflow code tracks several key components:

1. Parameters: It logs the Logistic Regression model maximum iterations and SVM hyperparameters.
2. Model: It saves the models.
3. Metrics: It captures and logs various metrics including accuracy, precision, recall, and F1-score.
4. Artifacts: It logs a heatmap of the confusion matrix for the model's predictions.

Only the top five models are registered based on their evaluation scores.

### Launching the MLflow UI

To monitor and visualize the experiment, use the MLflow UI.

To connect to the MLflow UI from Google Colab, use ngrok - a tool that creates secure tunnels from your any machine to the web - to create a tunnel on port 5000 and obtain a public URL. This URL lets you access the MLflow Tracking UI directly from your browser.
