import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

with open('html/2022_2023.html', 'r', encoding='utf-8') as f:
    gm = f.read()

soup = BeautifulSoup(gm, 'html.parser')
table = soup.find('table', id="matchlogs_for").find('tbody')
rows = table.find_all('tr')

games_dict = []
games = []

for row in rows:
    date_th = row.find('th')
    time_td = row.find_all('td')[0]
    comp_td = row.find_all('td')[1]
    round_td = row.find_all('td')[2]
    day_td = row.find_all('td')[3]
    venue_td = row.find_all('td')[4]
    result_td = row.find_all('td')[5]
    goals_for_td = row.find_all('td')[6]
    goals_against_td = row.find_all('td')[7]
    opponent_td = row.find_all('td')[8]
    xg_for_td = row.find_all('td')[9]
    xg_against_td = row.find_all('td')[10]
    possession_td = row.find_all('td')[11]
    attendance_td = row.find_all('td')[12]
    captain_td = row.find_all('td')[13]
    formation_td = row.find_all('td')[14]
    referee_td = row.find_all('td')[15]
    match_report_td = row.find_all('td')[16]
    notes_td = row.find_all('td')[17]

    games_dict = {
                'date'       : date_th.text,
                'start_time' : time_td.text,
                'comp'       : comp_td.text,
                'round'      : round_td.text,
                'day_tr'     : day_td.text,
                'venue'      : venue_td.text,
                'result'     : result_td.text,
                'goals_for'  : goals_for_td.text,
                'gL_against' : goals_against_td.text,
                'opponent'   : opponent_td.text,
                'xg_for_td'  : xg_for_td.text,
                'xg_against' : xg_against_td.text,
                'possession' : possession_td.text,
                'attendance' : attendance_td.text,
                'captain'    : captain_td.text,
                'formation'  : formation_td.text,
                'referee'    : referee_td.text,
                'report'     : match_report_td.text,
                'notes'      : notes_td.text
            }
    print(games_dict)
    games.append(games_dict)

with open("json/2022_2023.json", 'w', encoding='utf-8') as json_file:
        json.dump(games, json_file, ensure_ascii = False, indent =4, sort_keys=True)


