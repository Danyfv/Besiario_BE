import sqlite3

connnection = sqlite3.connect('database.db')


with open('sql/modificaDb.sql') as f:
    connnection.executescript(f.read())

with open('sql/query.sql') as f:
    connnection.executescript(f.read())


connnection.commit()
connnection.close()