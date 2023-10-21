class Medal:
    def __init__(self, student_id, subject_id, medal_type):
        # Конструктор класса инициализирует объект Medal с переданными атрибутами:
        # student_id - идентификатор студента
        # subject_id - идентификатор предмета
        # medal_type - тип медали
        self.student_id = student_id
        self.subject_id = subject_id
        self.medal_type = medal_type

    def save_to_database(self, db_manager):
        # Метод save_to_database выполняет вставку информации о медали в базу данных.
        # Он использует переданный объект db_manager класса DatabaseManager
        # для выполнения SQL-запроса INSERT INTO medals.
        # Значения для вставки берутся из атрибутов объекта Medal.
        query = "INSERT INTO medals (student_id, subject_id, medal_type) VALUES (%s, %s, %s)"
        values = (self.student_id, self.subject_id, self.medal_type)
        db_manager.execute_query(query, values)

