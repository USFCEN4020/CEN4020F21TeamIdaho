import sqlite3

##### Create the Database if it doesn't exist
with sqlite3.connect("User.db") as db:
    cursor = db.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username   VARCHAR(20) NOT NULL,
password   VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name  VARCHAR(20) NOT NULL); 
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS profiles(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
title VARCHAR(20),
major VARCHAR(20),
university VARCHAR(50),
about VARCHAR(250));
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS jobs(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
title VARCHAR(20),
employer VARCHAR(20),
started VARCHAR(20),
ended VARCHAR(20),
location VARCHAR(20),
description VARCHAR(250));
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS education(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
school VARCHAR(50),
degree VARCHAR(50),
years INTEGER);
"""
)

#status: 1. sentpending
#        2. acceptpending
#        3. friend
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS friends(
username VARCHAR(20) NOT NULL,
stranger VARCHAR(20) NOT NULL,
status VARCHAR(20));
"""
)

cursor.close()