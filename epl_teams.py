import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os.path

url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(url)

path = os.path.exists('html/teams.html')

if path != True:
    with open("html/teams.html", "w", encoding="utf-8") as f:
        f.write(data.text)
else:
    print("this file allready exists!")

with open("html/teams.html", 'r', encoding='utf-8') as f:
    page = f.read()
# print(page)

soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', id="results2022-202391_overall").find('tbody')
rows = table.find_all('tr')

names = []
teams = []
teams_dict = {}

home_url = "https://fbref.com"

for row in rows:
    td = row.find_all('td')
    links = row.find_all('a')[0]
    link = links.get('href')
    team_name = links.text
    if ' ' in team_name:
        team_name = team_name.replace(' ', '-')
    else:
        team_name = links.text

    # teams_dict['name'] = team_name
    # teams_dict['link'] = link

    teams_dict = {
        'link': home_url + link,
        'name': team_name
    }

    names.append(team_name)
    teams.append(teams_dict)

# print(names)

with open("json/teams.json", 'w', encoding='utf-8') as json_file:
    json.dump(teams, json_file, ensure_ascii = False, indent =4, sort_keys=False)
   
