import sqlite3
conn = sqlite3.connect("cleanfile.db")
cur = conn.cursor()

sql = """
CREATE TABLE weather_data(
station VARCHAR(20),
date DATE,
precip DECIMAL (4,2),
tobs INTEGER,
FOREIGN KEY (station) REFERENCES stations(station)
)"""

cur.execute(sql)
print("Tabela została stworzona")
conn.commit()
conn.close()