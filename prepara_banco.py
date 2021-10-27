import pandas as pd
from sqlalchemy import create_engine

equipments = pd.read_excel(r'equipment.xlsx')

engine = create_engine('sqlite:///db.sqlite3', echo=True)
sqlite_connection = engine.connect()

sqlite_table = "equipment"
equipments.to_sql(sqlite_table, sqlite_connection, if_exists='replace')

sqlite_connection.close()
