import sqlite3
import pandas as pd

conn = sqlite3.connect("cleanfile.db")

stations_df = pd.read_csv('clean_stations.csv')
stations_df.to_sql('stations', conn, if_exists = 'append', index=False)

weather_df = pd.read_csv('clean_measure.csv')
weather_df.to_sql('weather_data', conn, if_exists = 'append', index=False)

conn.commit()
conn.close()