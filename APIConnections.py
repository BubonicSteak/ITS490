import json
import requests
import subprocess
import os

# Endpoints
funguildEndpoint = "https://www.mycoportal.org/funguild/services/api/db_return.php"
fdexEndpoint = "https://www.mycoportal.org/fdex/services/api/query.php"

# Parameters
paramsFun = {
    'qField': 'taxonomicLevel',
    'qText': '13'
}

paramsDex = {
    'qField': 'rankCode',
    'qText': '13'
}

# Function to open files 
def openFile(filename):
    if os.name == 'nt':  # Windows
        os.startfile(filename)
    elif os.name == 'posix':  # macOS, Linux
        subprocess.run(['open' if os.uname().sysname == 'Darwin' else 'xdg-open', filename])

# Generate the response
funguildResponse = requests.get(funguildEndpoint, params=paramsFun)
fdexResponse = requests.get(fdexEndpoint, params=paramsDex)

# Extract taxon names for FUNGuild
def extractFunguildTaxonNames(data):
    if isinstance(data, list):
        taxonNames = [entry['taxon'] for entry in data if 'taxon' in entry]
        return taxonNames
    else:
        return []

# Extract taxon names for FDex data
def extractFdexTaxonNames(data):
    if isinstance(data, list):
        taxonNames = [entry['taxon'] for entry in data if 'taxon' in entry and entry.get('rankCode') == '13']
        return taxonNames
    else:
        return []

# Process FUNGuild 
if funguildResponse.status_code == 200:
    funguildData = funguildResponse.json()
    funguildTaxonNames = extractFunguildTaxonNames(funguildData)
    print("FUNGuild Taxon Names:", funguildTaxonNames)
    funguildFilename = 'funguild_taxonNames.json'  # Save to file
    with open(funguildFilename, 'w') as file:
        json.dump(funguildTaxonNames, file, indent=4)
    openFile(funguildFilename)
else:
    print("Error accessing FUNGuild API. Status code:", funguildResponse.status_code)

# Process FDex 
if fdexResponse.status_code == 200:
    try:
        fdexData = fdexResponse.json()
        fdexTaxonNames = extractFdexTaxonNames(fdexData)
        print("FDex Taxon Names:", fdexTaxonNames)
        if fdexTaxonNames:
            fdexFilename = 'fdex_taxonNames.json' # Save to file if not empty
            with open(fdexFilename, 'w') as file:
                json.dump(fdexTaxonNames, file, indent=4)
            openFile(fdexFilename)
        else:
            print("No taxon names.")
    except json.JSONDecodeError:
        print("Failed to decode FDex response as JSON. Response was:", fdexResponse.text)
else:
    print("Error accessing FDex API. Status code:", fdexResponse.status_code)
