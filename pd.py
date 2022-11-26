import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
# from main import *

standing_urls = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standing_urls)

soup = BeautifulSoup(data.text)
standing_table = soup.select('table.stats_table')[0]
links = standing_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
# grab all teams main stat links
team_urls = [f"https://fbref.com{l}" for l in links]
# the first team link
team_url = team_urls[0]
# get html of the team link
data = requests.get(team_url)
# print(data.text)

# Pandas method to parse HTML and create dataframe / Grab Score & Fixtures table
matches = pd.read_html(data.text, match="Scores & Fixtures")
# print(matches[0])

# Get Shooting stats table jf the team page
soup = BeautifulSoup(data.text)
links = soup.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if l and 'all_comps/shooting' in l]
# get url and html jf shooting page
data = requests.get(f"https://fbref.com{links[0]}")
shooting = pd.read_html(data.text, match="Shooting")[0]
print(shooting.head(5))