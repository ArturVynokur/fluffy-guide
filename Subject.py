class Subject:
    def __init__(self, subject_id, subject_name):
        # Конструктор класса инициализирует объект Subject с переданными атрибутами:
        # subject_id - идентификатор предмета
        # subject_name - имя предмета
        self.subject_name = subject_name
        self.subject_id = subject_id

    def save_to_database(self, db_manager):
        # Метод save_to_database выполняет вставку информации о предмете в базу данных.
        # Он использует переданный объект db_manager класса DatabaseManager
        # для выполнения SQL-запроса INSERT INTO subjects.
        # Значение для вставки берется из атрибута объекта Subject.
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        values = (self.subject_name,)
        db_manager.execute_query(query, values)
