import requests
import json
config = ""
with open("config.json","r") as config_file:
    config = json.load(config_file)

session = requests.session()
cookies = {
    'XSRF-TOKEN':f"{config['xsrf']}",
    'hellcase_session':f"{config['session']}"
}

session.cookies.update(cookies)

url = "https://api.hellcase.com/dailyfree/buy"
response = session.get(url)
print(response.text)
