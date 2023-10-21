class Grade:
    def __init__(self, grade_id, student_id, subject_id, grade):
        # Конструктор класса инициализирует объект Grade с переданными атрибутами:
        # grade_id - идентификатор оценки
        # student_id - идентификатор студента
        # subject_id - идентификатор предмета
        # grade - значение оценки
        self.grade_id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade

    def save_to_database(self, db_manager):
        # Метод save_to_database выполняет вставку информации о оценке в базу данных.
        # Он использует переданный объект db_manager класса DatabaseManager
        # для выполнения SQL-запроса INSERT INTO grades.
        # Значения для вставки берутся из атрибутов объекта Grade.
        query = "INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)"
        values = (self.student_id, self.subject_id, self.grade)
        db_manager.execute_query(query, values)

    def show_all(self, db_manager):
        # Метод show_all, возможно, должен выполнять запрос к базе данных
        # для получения информации о всех оценках, но в текущей реализации
        # он выполняет SQL-запрос, но не обрабатывает результаты и не возвращает их.
        # Вам может потребоваться изменить этот метод для обработки и возврата данных о всех оценках.
        query = 'SELECT * FROM grades '
        db_manager.execute_query(query)
