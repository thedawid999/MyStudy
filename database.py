import sqlite3
from course import Course

# noinspection SqlNoDataSourceInspection
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("mystudy.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
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
                grade REAL DEFAULT 0,
            )
        ''')

    #----------------------Methods for Course Database----------------------
    def add_course(self, course:Course):
        """adds a course to the database, if a grade for this course exists it will be added too"""
        if course.grade is not 0:
            self.cursor.execute("INSERT INTO course (name, grade) VALUES (?, ?)", (course.name, course.grade))
        else:
            self.cursor.execute("INSERT INTO course (name) VALUES (?)", course.name)
        self.conn.commit()

    def delete_course(self, course:Course):
        """deletes a course from the database"""
        self.cursor.execute("DELETE FROM course WHERE name = ?", course.name)
        self.conn.commit()

    def add_grade(self, course:Course):
        """adds a grade to its course"""
        self.cursor.execute("UPDATE course SET grade = ? WHERE name = ?", (course.grade, course.name))

    def delete_grade(self, course:Course):
        """deletes a grade from the database"""
        self.cursor.execute("UPDATE course SET grade = 0 WHERE name = ?", course.name)


    #----------------------Methods for TimeGoal Database----------------------
    ###

    #----------------------Methods for ValueGoal Database----------------------
    ###
