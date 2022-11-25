import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from epl_teams import names

for name in names:
    try:
        with open(f'html/{name}.html', 'r', encoding='utf-8') as f:
            gm = f.read()
   

        soup = BeautifulSoup(gm, 'html.parser')
        table = soup.find('table', id="matchlogs_for").find('tbody')
        rows = table.find_all('tr')

        home_url = "https://fbref.com"

        games_dict = []
        games = []

        for row in rows:
            # date
            date_th = row.find('th')
            # link 0
            date_link = row.find_all('a')[0]
            date_link = date_link.get('href')
            date_link =  f'https://fbref.com{date_link}'
            # time
            time_td = row.find_all('td')[0]
            # competition
            comp_td = row.find_all('td')[1]
            # link 1
            comp_link = row.find_all('a')[1]
            comp_link = comp_link.get('href')
            comp_link =  f'https://fbref.com{comp_link}'
            # round
            round_td = row.find_all('td')[2]
            # link 2
            round_link = row.find_all('a')[2]
            round_link = round_link.get('href')
            round_link =  f'https://fbref.com{round_link}'
            # day
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
                        'date_link'  : date_link,
                        'start_time' : time_td.text,
                        'comp'       : comp_td.text,
                        'comp_link'  : comp_link,
                        'round'      : round_td.text,
                        'round_link' : round_link,
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
            # print(games_dict)
            games.append(games_dict)

        with open(f"json/{name}.json", 'w', encoding='utf-8') as json_file:
                json.dump(games, json_file, ensure_ascii = False, indent =4, sort_keys=False)

    except:
        print(f'This team does not exist: {name}')
