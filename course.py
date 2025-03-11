from database import Database

class Course:
    def __init__(self, name:str, grade:float, db:Database):
        self._name = name
        self._grade = grade
        self._db = db

    def get_name(self):
        return self._name

    def get_grade(self):
        return self._grade

    def add_grade(self, grade:float):
        #define method!
        return None

    def delete_grade(self):
        #define method!
        return None