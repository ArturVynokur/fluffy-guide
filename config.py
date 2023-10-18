import mysql.connector

config = {
    'user': 'u743034853_artur_user',
    'password': '123Qwe!23',
    'host': '45.84.205.204',
    'database': 'u743034853_artur_db',
    'raise_on_warnings': True
}

# Підключення до бази даних
connection = mysql.connector.connect(**config)
