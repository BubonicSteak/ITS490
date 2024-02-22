import requests
import openai

# Endpoints
funguild_endpoint = "https://www.mycoportal.org/funguild/services/api/db_return.php"
fdex_endpoint = "https://www.mycoportal.org/fdex/services/api/query.php"


#GPT Key
openai.api_key = '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'


# Paramaters
params = {
    'qField': 'taxon',
    'qText': 'Magnaporthe'
}

# Generate the response
funguild_response = requests.get(funguild_endpoint, params=params)
fdex_response = requests.get(fdex_endpoint, params=params)


# Print data if found
if funguild_response.status_code == 200:
    funguild_data = funguild_response.json()
    print("FUNGuild Data:", funguild_data)
else:
    print("Error accessing FUNGuild API. Status code:", funguild_response.status_code)

if fdex_response.status_code == 200:
    fdex_data = fdex_response.json()

    print("fdex Data:", fdex_data)
else:
    print("Error accessing fdex API. Status code:", fdex_response.status_code)



#GPT Response
response = openai.Completion.create(
    model="text-davinci-002",  
    prompt="Tell me a joke",
    max_tokens=5  
)
