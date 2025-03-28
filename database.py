import sqlite3
from typing import TYPE_CHECKING
from time_goal import TimeGoal
from value_goal import ValueGoal

if TYPE_CHECKING:
    from goal import Goal
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
            CREATE TABLE IF NOT EXISTS timegoals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                startdate TEXT NOT NULL,
                deadline TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS valuegoals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                grade REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                grade REAL DEFAULT 0
            )
        ''')

    # ----------------------General----------------------
    def is_table_empty(self, table: str):
        """checks if a table is empty"""
        self.cursor.execute("SELECT count(*) FROM "+table)
        count = self.cursor.fetchone()[0]
        return count == 0

    def delete_student(self):
        """deletes all data"""
        self.cursor.execute("DROP TABLE timegoals")
        self.cursor.execute("DROP TABLE  valuegoals")
        self.cursor.execute("DROP TABLE  courses")
        #self.cursor.execute("DROP TABLE  sqlite_sequence")

    #----------------------Methods for Course Database----------------------
    def add_course(self, course:"Course"):
        """adds a course to the database, if a grade for this course exists it will be added too"""
        if course.get_grade() != 0:
            self.cursor.execute("INSERT INTO courses (title, grade) VALUES (?, ?)", (course.get_name(), course.get_grade()))
        else:
            self.cursor.execute("INSERT INTO courses (title) VALUES (?)", (course.get_name(),))
        self.conn.commit()

    def delete_course(self, course:"Course"):
        """deletes a course from the database"""
        self.cursor.execute("DELETE FROM courses WHERE title = ?", (course.get_name(),))
        self.conn.commit()

    def add_grade(self, course:"Course"):
        """adds a grade to its course"""
        self.cursor.execute("UPDATE courses SET grade = ? WHERE title = ?", (course.get_grade(), course.get_name()))
        self.conn.commit()

    def delete_grade(self, course:"Course"):
        """deletes a grade from the database"""
        self.cursor.execute("UPDATE courses SET grade = 0 WHERE title = ?", (course.get_name(),))
        self.conn.commit()

    def get_courses(self):
        """returns all courses from database if any exists"""
        if self.is_table_empty("courses"):
            return []
        else:
            self.cursor.execute("SELECT title,grade FROM courses")
            return self.cursor.fetchall()

    #----------------------Methods for TimeGoal and ValueGoal Database----------------------
    def add_goal(self, goal: "Goal"):
        """adds a TimeGoal or ValueGoal to the database"""
        if isinstance(goal, TimeGoal):
            self.cursor.execute("INSERT INTO timegoals (title, startdate, deadline) VALUES (?,?,?)",
                                (goal.get_title(), goal.get_startdate(), goal.get_deadline()))
        elif isinstance(goal, ValueGoal):
            self.cursor.execute("INSERT INTO valuegoals (title, grade) VALUES (?,?)",
                                (goal.get_title(), goal.get_value()))
        else:
            raise TypeError("Goal must be of type TimeGoal or ValueGoal")
        self.conn.commit()

    def delete_goal(self, goal:"Goal"):
        """deletes a time goal from the database"""
        if isinstance(goal, TimeGoal):
            self.cursor.execute("DELETE FROM timegoals WHERE title = ?", (goal.get_title(),))
        elif isinstance(goal, ValueGoal):
            self.cursor.execute("DELETE FROM valuegoals WHERE title = ?", (goal.get_title(),))
        else:
            raise TypeError("Goal must be of type TimeGoal or ValueGoal")
        self.conn.commit()

    def get_time_goals(self):
        """returns all time goals from database if any exists"""
        if self.is_table_empty("timegoals"):
            return []
        else:
            self.cursor.execute("SELECT title, startdate, deadline FROM timegoals")
            return self.cursor.fetchall()

    def get_value_goals(self):
        """returns all value goals from database if any exists"""
        if self.is_table_empty("valuegoals"):
            return []
        else:
            self.cursor.execute("SELECT title, grade FROM valuegoals")
            return self.cursor.fetchall()

    def close(self):
        """closes the database"""
        self.cursor.close()

