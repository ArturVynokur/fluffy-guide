class Student:
    def __init__(self, student_id, student_name, grades=None):
        # Конструктор класса инициализирует объект Student с переданными атрибутами:
        # student_id - идентификатор студента
        # student_name - имя студента
        # grades - список оценок (по умолчанию пустой список)
        self.grades = grades or []
        self.student_name = student_name
        self.student_id = student_id

    def save_to_database(self, db_manager):
        # Метод save_to_database выполняет вставку информации о студенте в базу данных.
        # Он использует переданный объект db_manager класса DatabaseManager
        # для выполнения SQL-запроса INSERT INTO students.
        # Значения для вставки берутся из атрибутов объекта Student.
        query = 'INSERT INTO students VALUES(%s, %s)'
        values = (self.student_id, self.student_name)
        db_manager.execute_query(query, values)

    @staticmethod
    def fetch_by_id(db_manager, student_id):
        # Статический метод fetch_by_id используется для получения информации о студенте
        # по его идентификатору из базы данных. Он вызывает метод fetch_student_by_id
        # из объекта db_manager класса DatabaseManager для выполнения SQL-запроса
        # и получения данных о студенте. Если данные о студенте найдены, создается
        # новый объект Student, и эти данные используются для его инициализации.
        # Если студент не найден, метод возвращает None.
        student_info = db_manager.fetch_student_by_id(student_id)
        if student_info:
            return Student(student_info["student_id"], student_info["student_name"], student_info["grades"])
        else:
            return None
