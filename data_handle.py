import pandas as pd

df_per = pd.read_csv('df_per.csv')

df_bio = pd.read_csv('bio_2002_2022.csv')
df_bio['year'] = df_bio['year'].str[:2] + df_bio['year'].str[-2:]
df_bio['year'] = df_bio['year'].astype(int)

df_map = pd.read_csv('country_mapping.csv')
dict_country = dict(zip(df_map.Country,df_map.Continent))


df_bio['continent'] = df_bio['COUNTRY'].map(dict_country)

df_merged = df_per.merge(df_bio,how='left',on=['PLAYER_NAME','year'])
columns = ['PLAYER_NAME','year','PER','COUNTRY','continent','AGE','DRAFT_YEAR']
df = df_merged[columns]

players_df_max_PER = df.loc[df.groupby('PLAYER_NAME')['PER'].idxmax()]
players_df_max_PER.rename(columns= {'year':'year_max_per','PER':'max_per'},inplace=True)

players_list_min_year = df.loc[df.groupby('PLAYER_NAME')['year'].idxmin()]
players_list_min_year.rename(columns= {'year':'player_min_year'},inplace=True)

new_df = df.merge(players_df_max_PER[['PLAYER_NAME','year_max_per','max_per']],how='left',on='PLAYER_NAME')
final_df = new_df.merge(players_list_min_year[['PLAYER_NAME','player_min_year']],how='left',on='PLAYER_NAME')

final_df = final_df.sort_values('year')

final_df.to_csv('final_df.csv', index=False)



#best_ten = df_merged.nlargest(40,'PER').reset_index()
#best_ten = best_ten[columns]



#melo = df_merged[df_merged['PLAYER_NAME'] == 'Carmelo Anthony']
#print(melo[columns])

#print(best_ten)
# print(df.year.value_counts())