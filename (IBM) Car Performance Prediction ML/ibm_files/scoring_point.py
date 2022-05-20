import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "XvwSj9qdy7B_gr4BNjwR4p7-hlUMoZSDWjwHjgqhYZ8s"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ['cylinders','displacement','horsepower','weight','acceleration','model year'], "values": [[8,440.0,215,4312,8.5,70]]}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/4551b24d-4ed8-457f-b3bc-62dafaefc7b7/predictions?version=2022-03-05', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())

op = response_scoring.json()

pred = op['predictions'][0]['values'][0][0]
pred = float("{:.2f}".format(pred))

print(pred)