import requests
import json
url = "https://api.hellcase.com/dailyfree/buy"
config = ""
with open("config.json","r") as config_file:
    config = json.load(config_file)

payload = ""
headers = {"cookie": f"XSRF-TOKEN={config['xsrf']}; hellcase_session={config['session']}"}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
