from database import Database
from reader import Reader
from student import Student
from visualizer import Visualizer


def main():
    db = Database()
    student = Student(db)
    Visualizer.set_student(student)

    #TODO: finish here
    #TODO: specify that max. 1 valuegoal and max. 3 timegoals can be added
    while True:
        Reader.read_input()

if __name__=="__main__":
    main()