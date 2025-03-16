from student import Student
from rich.table import Table
from rich.console import Console
from rich import print

class Visualizer:
    _student = None
    _table = Table()
    _table.add_column("Deadlines")
    _table.add_column("Progress")

    @staticmethod
    def set_student(student: Student):
        Visualizer._student = student

    @staticmethod
    def show_dashboard():
        #TODO: define method!
        print("MY STUDY DASHBOARD")
        print(Visualizer._table)
        return None

    @staticmethod
    def show_grades():
        #TODO: define method!
        return None

    @staticmethod
    def show_help():
        #TODO: define method!
        """
        A simple program to manage your courses, grades and goals

        Usage: [COMMAND] [ARGS]

        Commands:
          addcourse NAME                        Add a course only.
          addcourse NAME GRADE                  Add a course with a grade.
          delcourse NAME                        Remove a course by name.
          addgrade COURSENAME GRADE             Add a grade to an existing course.
          delgrade COURSENAME                   Remove a grade from an existing course.
          addgoal TITLE STARTDATE DEADLINE      Add a time goal, format of STARTDATE and DEADLINE is YYYYMMDD.
          addgoal TITLE VALUE                   Add a value goal.
          delgoal TITLE                         Remove a goal by title.
          help                                  Display all commands.
          showgrades                            Display all courses and grades.
          dashboard                             Display dashbaord (main screen).
          exit

        Examples:
          addcourse Mathematik:Analysis 2.1
          addgrade Informatik 3.0
          addgoal ProjektX 20250101 20250601
          addgoal Notenschnitt 1.5
        """

        return None