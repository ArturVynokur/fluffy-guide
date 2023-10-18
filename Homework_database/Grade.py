import config


class Grade:
    def __init__(self, grade_id, student_id, subject_id, grade):
        self.grade_id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade

    def save_to_database(self, db_manager):
        query = "INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)"
        values = (self.student_id, self.subject_id, self.grade)
        db_manager.execute_query(query, values)

    def show_all(self, db_manager):
        query = 'SELECT * FROM grades '
        db_manager.execute_query(query)
