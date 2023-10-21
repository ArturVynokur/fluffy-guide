class Medal:
    def __init__(self, student_id, subject_id, medal_type):
        self.student_id = student_id
        self.subject_id = subject_id
        self.medal_type = medal_type

    def save_to_database(self, db_manager):
        query = "INSERT INTO medals (student_id, subject_id, medal_type) VALUES (%s, %s, %s)"
        values = (self.student_id, self.subject_id, self.medal_type)
        db_manager.execute_query(query, values)

