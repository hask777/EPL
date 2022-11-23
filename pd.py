import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
# from main import *

# Work with pandas dataframe
matches = pd.read_html('html/games.html', match="Scores & Fixtures")
print(matches[0])


