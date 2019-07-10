import sqlite3

conn = sqlite3.connect('timetracking.db')

c = conn.cursor()
c.execute("""CREATE TABLE user (
                 uuid integr,
                 name text,
                 appear_date DATETIME,
                 training_session text
         ) """)