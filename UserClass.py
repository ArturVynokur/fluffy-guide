import config


class User:
    def __init__(self, id, name, mail, phone):
        self.id = id
        self.name = name
        self.phone = phone
        self.mail = mail

    def show_one(self):
        print(f"User ID: {self.id}")
        print(f"Username: {self.name}")
        print(f"Email: {self.mail}")
        print(f"Phone: {self.phone}")
        print("-" * 20)
    # %s - любая переменная
    @classmethod
    def load_by_id(cls, user_id):
        cursor = config.connection.cursor()
        query = 'SELECT id, name, email, phone FROM user WHERE id = %s'
        cursor.execute(query, (user_id,))
        # execute - делает запрос в бвзу данных
        # fetchall - выводит все записи
        user_data = cursor.fetchone()

        if user_data:
            return cls(user_data[0], user_data[1], user_data[2], user_data[3])
        else:
            return None
