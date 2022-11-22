import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"
data = requests.get(url)
# print(data.text)

soup = BeautifulSoup(data.text)
standings_table = soup.select('table.stats_table')[0]
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
teams_urls = [f"https://fbref.com{l}" for l in links]
team_url = teams_urls[0]
# print(team_url) ststus(s)

team_games = requests.get(team_url)

# This is full html of page
games_page = team_games.text

# Get a table
game_stat = {}

soup = BeautifulSoup(games_page)
games_table = soup.find('table', id="matchlogs_for")
table_body = games_table.find('tbody')
game_time = table_body.find_all('th')[0]
td = table_body.select('td[data-stat]')[0]
span = td.find('span', class_="venuetime")

game_stat = {
                "date": span.text,
            }
print(game_stat)









# here get pure html of the first team status(s)
# with open("games.html", "w+", encoding="utf-8") as f:
#     f.write(games)
# print(games)

   
    
