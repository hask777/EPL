import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('html/games.html', 'r', encoding='utf-8') as f:
    gm = f.read()

game_stat = {}

soup = BeautifulSoup(gm, 'html.parser')
games_table = soup.find('table', id="matchlogs_for")
table_body = games_table.find('tbody')
game_time = table_body.find_all('th')[0]
td = table_body.select('td[data-stat]')[0]
span = td.find('span', class_="venuetime")

game_stat = {
                "date": span.text,
            }
print(game_stat)