import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
start = time.time()
PATH = '/Users/urielf/Documents/chromedriver'
driver = webdriver.Chrome(PATH)
url_params = "http://www.espn.com/nba/hollinger/statistics/_/page/{page}/year/{year}"


def get_players_PER_stats(url,year,page=0):
    driver.get(url.format(page=page, year=year))

    src = driver.page_source
    parser = BeautifulSoup(src,"html.parser")

    p = parser.find_all(class_='page-numbers')[0]
    pages = p.text[-1]

    tag = parser.find_all(class_='colhead')[0]
    names = tag.find_all("td")
    headers_list = [n.text.strip() for n in names[1:]]

    table = parser.find_all(class_='tablehead')[0]
    rows = table.find_all("tr")[2:]
    player_stats = [[td.text.strip() for td in rows[i].find_all('td')[1:]] for i in range(len(rows))]

    PER_df = pd.DataFrame(player_stats,columns=headers_list)
    PER_df = PER_df.drop(PER_df[PER_df['PLAYER'] == 'PLAYER'].index)
    PER_df = PER_df.reset_index(drop=True)
    PER_df['year'] = year

    return PER_df,pages

driver.close()

