import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

s = random.randint(1, 40)
webData = requests.get('https://www.tvguide.com/streaming/all/comedy/show/1/?sort=highestRated&genre=comedy&type=show&releaseYearMin=2000&releaseYearMax=2020&page={0}'.format(s))
soup = BeautifulSoup(webData.content, 'html.parser')
l = list(soup.find_all('h3', class_='g-text-xlarge g-text-bold g-outer-spacing-bottom-xsmall'))

shows = []

while len(shows) < 5:
    rc = random.choice(l).get_text().strip()
    if rc in shows:
        continue
    shows.append(rc)

inData = pd.DataFrame({'Comedy Recommendations': shows})

inData.to_excel('tableData.xlsx', index = None)

outData = pd.read_excel('tableData.xlsx', engine = 'openpyxl', index_col = None)

print(outData)