#SQLite 3 page 

import sqlite3

with sqlite3.connect("User.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username   VARCHAR(20) NOT NULL,
password   VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name  VARCHAR(20) NOT NULL); 
""")

###################################################
# run this file if you want to empty the database #
###################################################

def emptyDatabase():
    db.commit()

    #enter SQL queries here
    cursor.execute("DELETE FROM user")
    db.commit()
