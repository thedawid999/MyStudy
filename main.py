from database import Database
from reader import Reader
from student import Student
from visualizer import Visualizer
import os

def main():
    os.system('cls')
    db = Database()

    try:
        student = Student(db)
        Visualizer.set_student(student)

        Visualizer.show_dashboard()
        while True:
            Reader.read_input()
    finally:
        db.close()

if __name__=="__main__":
    main()