import requests
import json
from datetime import datetime
config = ""
with open("config.json","r") as config_file:
    config = json.load(config_file)

session = requests.session()
cookies = {
    'XSRF-TOKEN':f"{config['xsrf']}",
    'hellcase_session':f"{config['session']}"
}

session.cookies.update(cookies)


url = "https://api.hellcase.com/main_page_giveaways"
response = session.get(url)
response_json = json.loads(response.text)
if not response_json['data']['free_giveaway']['is_user_joined']:
    print("TODO LOGIC WHEN NOT JOINED")
else:
    print("ALREADY JOINED, THIS GIVEAWAY ENDS IN")
    end_date = datetime.strptime(response_json['data']['free_giveaway']['finish'],"%Y-%m-%d %H:%M:%S")
    print(end_date - datetime.now())