import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerbiostats #Biography by Season, get Player ID
from nba_api.stats.endpoints import leaguedashplayerstats # Season stats by Player

def get_player_stats(season_year):
    df = leaguedashplayerstats.LeagueDashPlayerStats(season=season_year).get_data_frames()[0]
    return df

def get_player_bio(season_year):
    df = leaguedashplayerbiostats.LeagueDashPlayerBioStats(season=season_year).get_data_frames()[0]
    column_names = ['PLAYER_ID', 'PLAYER_NAME', 'DRAFT_YEAR', 'COUNTRY','AGE']
    df = df[column_names]
    df['year'] = season_year
    return df


