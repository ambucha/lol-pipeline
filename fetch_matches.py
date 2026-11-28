import os
import json
import pathlib
import requests
from dotenv import load_dotenv

load_dotenv()
HEADERS = {"X-Riot-Token": os.environ["RIOT_API_KEY"]}
BASE = "https://americas.api.riotgames.com"

def get(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

#1 get the puuid from Riot ID
name, tag = "boochboy", "NA1"
account = get(f"{BASE}/riot/account/v1/accounts/by-riot-id/{name}/{tag}")
puuid = account["puuid"]
print("puuid:", puuid)

#2 use the puuid to get the list of recent ranked solo/duo match IDs
match_ids = get(f"{BASE}/lol/match/v5/matches/by-puuid/{puuid}/ids", params={"queue": 420, "count": 5},) #get the last five ranked s/d games (420 is solo duo code)
print("match IDs:", match_ids)

#3 download the first match and save
match_id = match_ids[0]
match = get(f"{BASE}/lol/match/v5/matches/{match_id}")

folder = pathlib.Path("data/raw/matches")
folder.mkdir(parents=True, exist_ok=True)
(folder / f"{match_id}.json").write_text(json.dumps(match, indent=2))
print("saved", match_id)
