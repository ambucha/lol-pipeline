import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.environ["RIOT_API_KEY"]

name, tag = "boochboy", "NA1" #input riot ID here for testing
url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"

r = requests.get(url, headers = {"X-Riot-Token": key})
print(r.status_code)
print(r.json())
