class Subject:
    def __init__(self, subject_id, subject_name):
        self.subject_name = subject_name
        self.subject_id = subject_id

    def save_to_database(self, db_manager):
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        values = (self.subject_name,)
        db_manager.execute_query(query, values)
