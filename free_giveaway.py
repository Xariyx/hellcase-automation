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
headers = {
    "X-Requested-With": "XMLHttpRequest",
}


session.cookies.update(cookies)
session.headers.update(headers)

url_get = "https://api.hellcase.com/main_page_giveaways"
url_join = "https://api.hellcase.com/giveaway/join_social_giveaways/"
response = session.get(url_get)
response_json = json.loads(response.text)
if not response_json['data']['free_giveaway']['is_user_joined']:
    giveaway_id = str(response_json['data']['free_giveaway']['id'])
    response_join = session.get(url_join + giveaway_id)
    print(response_join.text)
    
else:
    print("ALREADY JOINED, THIS GIVEAWAY ENDS IN")
    end_date = datetime.strptime(response_json['data']['free_giveaway']['finish'],"%Y-%m-%d %H:%M:%S")
    print(end_date - datetime.now())