import sqlite3
conn = sqlite3.connect("cleanfile.db")
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS combined_data AS
            SELECT weather_data.station, weather_data.date, weather_data.precip, weather_data.tobs,
            stations.latitude, stations.longitude, stations.elevation, stations.name, stations.country,stations.state
            FROM weather_data
            JOIN stations ON weather_data.station = stations.station
            ''')

conn.commit()
conn.close()