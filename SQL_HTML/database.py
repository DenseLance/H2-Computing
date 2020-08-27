import os.path
import sqlite3

def create_user_table():
    db = sqlite3.connect("database.db")
    query = """
    CREATE TABLE UserInfo (
        username TEXT PRIMARY KEY UNIQUE NOT NULL,
        email TEXT,
        password TEXT
    )
    """
    db.execute(query)
    db.commit()
    db.close()

def create_forum_table():
    db = sqlite3.connect("database.db")
    query = """
    CREATE TABLE Forum (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT,
        message TEXT,
    
        FOREIGN KEY(username) REFERENCES UserInfo(username)
    )
    """
    db.execute(query)
    db.commit()
    db.close()

# creates table only if database file does not already exist
if not os.path.isfile("database.db"):
    create_user_table()
    create_forum_table()