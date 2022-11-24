import requests
from bs4 import BeautifulSoup
import pandas as pd
import os.path
from epl_teams import names

print(names)


url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"
data = requests.get(url)
# print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')

standings_table = soup.select('table.stats_table')[0]
# print(team)
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
teams_urls = [f"https://fbref.com{l}" for l in links]
team_url = teams_urls[0]
print(teams_urls)

team_games = requests.get(team_url)

# This is full html of page
games_page = team_games.text
# print(games_page)
# here get pure html of the first team status(s)
with open("html/teams.html", "w+", encoding="utf-8") as f:
    f.write(games_page)


   
    
