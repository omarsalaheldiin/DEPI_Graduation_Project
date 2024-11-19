This code provides a Flask application that leverages a pre-trained DistilBERT base uncased model finetuned on the SST-2 dataset for sentiment analysis. Users can input statement, and the application returns the predicted sentiment (positive or negative).

DistilBERT base uncased finetuned SST-2 model is a fine-tune checkpoint of DistilBERT-base-uncased, fine-tuned on SST-2. This model reaches an accuracy of 91.3 on the dev set (for comparison, Bert bert-base-uncased version reaches an accuracy of 92.7).


# Prerequisites:

Before running the main.py script, ensure you have the following python packages installed:

```bash
pip install -r requirements.txt
```

This will install necessary libraries like Azure Machine Learning SDK, Streamlit, and others listed in the requirements.txt file.



# Code Breakdown:

The main.py script handles the core functionality of the application.

# Azure Machine Learning Configuration

This section show the credentials that are essential to interact with your Azure Machine Learning workspace and resources.
Replace below with your actual Azure Machine Learning credentials and resources:
1. tenant_id: The unique identifier of Azure Active Directory tenant.
2. client_id: The unique identifier of Azure AD application.
3. client_secret: The secret key associated with Azure AD application.
4. subscription_id: The unique identifier of your Azure subscription.
5. resource_group: The logical container for Azure resources. 
6. workspace_name: The name of Azure Machine Learning workspace.

# Model Deployment

This section creates or updates a managed online endpoint for the DistilBERT model (distilbert-base-uncased-finetuned-sst-2-english).
Update the following details:
1. registry_name: Name of the Azure Machine Learning registry containing the model.
2. model_name: Specific name of the DistilBERT model.
3. version: Version of the DistilBERT model.
4. endpoint_name: Desired name for the online endpoint. (mandatory)

# Sentiment Application Setup 

This section handles the Sentiment logic of the sentiment analysis application.
It initializes a Sentiment application which allows to input review text into a text area and click a button to classify the sentiment of their input as positive or negative. The app sends this input to the model deployment endpoint for processing, displays the resulting sentiment and its score on Streamlit's web interface.
