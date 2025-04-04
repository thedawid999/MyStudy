class Course:
    def __init__(self, name:str, db,grade:float=0):
        self._name = name
        self._db = db
        self._grade = grade

    def get_name(self):
        """returns Course name"""
        return self._name

    def get_grade(self):
        """returns Course grade"""
        return self._grade

    def add_grade(self, grade:float):
        """adds a new grade"""
        self._grade = grade
        self._db.add_grade(self)

    def delete_grade(self):
        """deletes a grade"""
        self._grade = 0
        self._db.delete_grade(self)
        return None

    @staticmethod
    def to_course(data, db):
        """converts db-data into a Course object"""
        return Course(data[0], db, data[1])