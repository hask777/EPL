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
# print(f'{teams_urls}\n')

for team_url in teams_urls:
    print(team_url)
    # team_page = requests.get(team_url)
    # team_soup = BeautifulSoup(team_page.text)
    # print(team_soup)

# team_games = requests.get(team_url)

# # This is full html of page
# games_page = team_games.text
# # print(games_page)
# # here get pure html of the first team status(s)
# with open("html/2022_2033.html", "w+", encoding="utf-8") as f:
#     f.write(games_page)
# print(games_page)
