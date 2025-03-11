import sqlite3
from course import Course
from time_goal import TimeGoal
from value_goal import ValueGoal


# noinspection SqlNoDataSourceInspection
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("mystudy.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """creates tables for courses, value goals and time goals"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS timegoals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                startdate TEXT NOT NULL,
                deadline TEXT NOT NULL,   
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS valuegoals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                value REAL NOT NULL,
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade REAL DEFAULT 0,
            )
        ''')

    #----------------------Methods for Course Database----------------------
    def add_course(self, course:Course):
        """adds a course to the database, if a grade for this course exists it will be added too"""
        if course.get_grade() is not 0:
            self.cursor.execute("INSERT INTO courses (name, grade) VALUES (?, ?)", (course.get_name(), course.get_grade()))
        else:
            self.cursor.execute("INSERT INTO courses (name) VALUES (?)", course.get_name())
        self.conn.commit()

    def delete_course(self, course:Course):
        """deletes a course from the database"""
        self.cursor.execute("DELETE FROM courses WHERE name = ?", course.get_name())
        self.conn.commit()

    def add_grade(self, course:Course):
        """adds a grade to its course"""
        self.cursor.execute("UPDATE courses SET grade = ? WHERE name = ?", (course.get_grade(), course.get_name()))
        self.conn.commit()

    def delete_grade(self, course:Course):
        """deletes a grade from the database"""
        self.cursor.execute("UPDATE courses SET grade = 0 WHERE name = ?", course.get_name())
        self.conn.commit()

    def get_courses(self):
        """returns all courses from database"""
        self.cursor.execute("SELECT name,grade FROM courses")
        return self.cursor.fetchall()

    #----------------------Methods for TimeGoal Database----------------------
    def add_time_goal(self, timegoal: TimeGoal):
        self.cursor.execute("INSERT INTO timegoals (title, startdate, deadline) VALUES (?,?,?)",
                            (timegoal.get_title(), timegoal.get_startdate(), timegoal.get_deadline()))
        self.conn.commit()

    def delete_time_goal(self, timegoal:TimeGoal):
        self.cursor.execute("DELETE FROM timegoals WHERE title = ?", timegoal.get_title())
        self.conn.commit()

    def get_time_goals(self):
        self.cursor.execute("SELECT title, startdate, deadline FROM timegoals")
        return self.cursor.fetchall()

    #----------------------Methods for ValueGoal Database----------------------
    def add_value_goal(self, valuegoal:ValueGoal):
        self.cursor.execute("INSERT INTO valuegoals (title, value) VALUES (?,?)",
                            (valuegoal.get_title(), valuegoal.get_value()))
        self.conn.commit()

    def delete_value_goal(self, valuegoal:ValueGoal):
        self.cursor.execute("DELETE FROM valuegoals WHERE title = ?", valuegoal.get_title())
        self.conn.commit()

    def get_value_goals(self):
        self.cursor.execute("SELECT title, value FROM valuegoals")
        return self.cursor.fetchall()
