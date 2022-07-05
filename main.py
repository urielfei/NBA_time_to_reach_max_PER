import pandas as pd
from get_data_from_nbaApi import get_player_bio
from Scrape_data_from_ESPN import get_players_PER_stats, url_params

#### Get Players BIO from NBA API ####
years = ['2002-03'
    #,'2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12',
    #    '2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22'
         ]

df = pd.DataFrame()
for year in years:
   raw = get_player_bio(year)
   df = df.append(raw)

df.to_csv('bio_2002_2022.csv')

#### Get Players PER Stats from ESPN ####
years = ['2009']
counter = 0
for year in years:
    pages = range(1, int(get_players_PER_stats(url_params,year)[1]) + 1)
    for page in pages:
        if page == 1 and counter == 0:
            df = get_players_PER_stats(url_params,year,page)[0]
            counter += 1
        else:
            df_time = get_players_PER_stats(url_params,year,page)[0]
            df = df.append(df_time)

df.to_csv('df_per.csv',index=False)