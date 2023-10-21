class Student:
    def __init__(self, student_id, student_name, grades=None):
        self.grades = grades or []
        self.student_name = student_name
        self.student_id = student_id

    def save_to_database(self, db_manager):
        query = 'INSERT INTO students VALUES(%s, %s)'
        values = (self.student_id, self.student_name)
        db_manager.execute_query(query, values)

    @staticmethod
    def fetch_by_id(db_manager, student_id):
        student_info = db_manager.fetch_student_by_id(student_id)
        if student_info:
            return Student(student_info["student_id"], student_info["student_name"], student_info["grades"])
        else:
            return None

