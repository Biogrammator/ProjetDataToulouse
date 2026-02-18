import requests
server = "https://data.toulouse-metropole.fr/api/explore/v2.1"
endpoint = "/catalog/datasets/inventaire-de-la-flore-sauvage-en-milieu-urbain-ville-de-toulouse/records"

api_url = server + endpoint
print(api_url)

response = requests.get(api_url)

# Affichage
#print(response.json())
print(response.json)

print(response.status_code)
print(response.headers["Content-Type"])

