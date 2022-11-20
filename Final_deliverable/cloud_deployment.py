from ibm_watson_machine_learning import APIClient

wml_credentials = { 
    "url": "https://us-south.ml.cloud.ibm.com", 
    "apikey":"049g5 rjLtMfFoxPrBuja8eQPmNZtIK-uGy3 Mzolzp"}

client = APIClient (wml_credentials)

client = APIClient (wml_credentials)

def giud_from_space_name (client, space_name): 
    space = client.spaces.get_details()

    return (next (item for item in space ['resources'] if 
item['entity']['name'] == space_name) ['metadata']['id'])

space_uid= giud_from_space_name (client, 'Nutrition Analyzer') 
print ("Space UID ",+ space_uid)

client.set.default_space (space_uid)

client.repository.download('4e26ad0-bb0c-4b3d-8476-963013617dc21','my model.tar.gzt')