import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("mystudy.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_table(self):
        """creates tables for courses, value goals and time goals"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS timegoal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                startdate TEXT NOT NULL,
                deadline TEXT NOT NULL,   
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS valuegoal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                value REAL NOT NULL,
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS course (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade REAL NOT NULL,
            )
        ''')