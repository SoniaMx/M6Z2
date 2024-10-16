import sqlite3
conn = sqlite3.connect("cleanfile.db")
cur = conn.cursor()

sql = """
CREATE TABLE stations(
station VARCHAR(20) PRIMARY KEY,
latitude DECIMAL (7,4),
longitude DECIMAL (7,4),
elevation DECIMAL(5,2),
name VARCHAR (100),
country CHAR (2),
state CHAR (2)
)"""

cur.execute(sql)
print("Tabela została stworzona")
conn.commit()
conn.close()