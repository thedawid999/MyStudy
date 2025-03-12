from database import Database

class Course:
    def __init__(self, name:str, db:Database,grade:float=0):
        self._name = name
        self._db = db
        self._grade = grade

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