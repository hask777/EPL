import requests
from bs4 import BeautifulSoup
import pandas as pd
from main import *

# Work with pandas dataframe
matches = pd.read_html(data.text, match="Scores & Fixtures")
# print(matches[0])