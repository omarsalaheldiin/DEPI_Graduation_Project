import time
import requests
import streamlit as st

from azure.ai.ml import MLClient
from azure.identity import ClientSecretCredential

from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration,
)


### Azure Machine Learning Configuration ####

# Replace with your Azure Machine Learning credentials
tenant_id = ""  # Your Azure Tenant ID
client_id = ""    # Your Azure Client ID
client_secret = ""  # Your Azure Client Secret

subscription_id = ""  # Your Azure Subscription ID
resource_group = ""   # Your Azure Resource Group
workspace_name = ""  # Your Azure Machine Learning Workspace Name

credential = ClientSecretCredential(tenant_id, client_id, client_secret)
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)


### Model Deployment ####

registry_name = "azureml"  # Name of the Azure Machine Learning registry
model_name = "distilbert-base-uncased-finetuned-sst-2-english"  # Specific DistilBERT model name
version = 13  # Version of the DistilBERT model

model_id = f"azureml://registries/{registry_name}/models/{model_name}/versions/{version}"

endpoint_name = ""  # Desired name for the online endpoint
ml_client.begin_create_or_update(ManagedOnlineEndpoint(name=endpoint_name))
time.sleep(10)

ml_client.online_deployments.begin_create_or_update(ManagedOnlineDeployment(
    name="beta",
    endpoint_name=endpoint_name,
    model=model_id,
    instance_type="Standard_F8s_v2",
    instance_count=1,
))
time.sleep(600)

endpoint = ml_client.online_endpoints.get(endpoint_name)
endpoint.traffic = {"beta": 100}
ml_client.begin_create_or_update(endpoint)
time.sleep(60)


### Streamlit Application Setup ###

endpoint_url = endpoint.scoring_uri 
key = ml_client.online_endpoints.get_keys(name=endpoint_name).primary_key

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {key}'
}

st.title("DEPI Graduation: Sentiment Analysis App")
st.write("Enter a review to see if it's Positive or Negative.") 

input_data = st.text_area("Review Text", height=150) # Create a text area for user input

if st.button("Classify"):
    if input_data:
        json_data = {
            "input_data": [
                input_data
            ]
        }
        response = requests.post(endpoint_url, headers=headers, json=json_data)
        response.raise_for_status()
        res = response.json()[0]
        st.success(f"Sentiment: {res['label']}")
        st.success(f"Score: {res['score']}")

    else:
        st.error("Please enter a statement to analyze.")