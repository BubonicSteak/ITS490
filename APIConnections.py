import requests
import openai
from openai import OpenAI

# Endpoints
funguild_endpoint = "https://www.mycoportal.org/funguild/services/api/db_return.php"
fdex_endpoint = "https://www.mycoportal.org/fdex/services/api/query.php"

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


client = OpenAI(
  api_key= "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")

#GPT Response
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop."
)
