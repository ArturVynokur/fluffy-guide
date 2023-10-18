from Homework_database.DatabaseManager import DatabaseManager
# from Homework_database.Grade import Grade
# from Homework_database.Medal import Medal
# from Homework_database.Students import Student
# from Homework_database.Subject import Subject
# import json
# import random

db_manager = DatabaseManager(
    host='45.84.205.204',
    password='123Qwe!23',
    user='u743034853_artur_user',
    database='u743034853_artur_db'
)
"""with open('student.json') as f:
    data = json.load(f)

# Сохранение студентов, предметов и оценок в базе данных
for student_data in data["students"]:
    student_id = student_data["student_id"]
    student_name = student_data["student_name"]

    # Проверка существования студента в базе данных
    query_check = "SELECT * FROM students WHERE student_id = %s"
    values_check = (student_id,)
    existing_student = db_manager.fetch_query(query_check, values_check)

    if not existing_student:
        # Если студента нет, добавляем нового
        student = Student(student_id, student_name)
        student.save_to_database(db_manager)
    else:
        # Если студент существует, можно обновить его данные
        query_update = "UPDATE students SET student_name = %s WHERE student_id = %s"
        values_update = (student_name, student_id)
        db_manager.execute_query(query_update, values_update)

    for grade_data in student_data["grades"]:
        subject_id = grade_data['subject_id']
        subject_name = grade_data["subject"]
        grade = grade_data["grade"]

        subject = Subject(subject_id, subject_name)

        grade = Grade(None, student_id, subject_id, grade)
        grade.save_to_database(db_manager)

# Закрытие соединения с базой данных
db_manager.close()"""

"""
Студенты-> (завтра на уроке)
    Группа +

Вывод -> (домашка)
    Отдельно
    Отличники
    Самая +
    Самая -
"""
# student_id_to_find = int(input("Введите ID студента: "))
# found_student = Student.fetch_by_id(db_manager, student_id_to_find)
#
# if found_student:
#     print(f"Найденый студент: id({found_student.student_id}), {found_student.student_name}")
#     for grade_info in found_student.grades:
#         print(f"Subject: {grade_info['subject']}, Grade: {grade_info['grade']}")
#
# else:
#     print(f"Студент с ID({student_id_to_find}) не найден")
#
# # Получение отличников (предположим, отличник - это студент с оценками выше или равными 90)
# excellent_students = db_manager.fetch_excellent_students(90)
# # Вывод результатов
# print("Excellent Students:")
# for student_info in excellent_students:
#     print("Student ID:", student_info["student_id"])
#     print("Student Name:", student_info["student_name"])
#     print("Grades:")
#     for grade_info in student_info["grades"]:
#         print(f"Subject: {grade_info['subject']}, Grade: {grade_info['grade']}")
#     print("---")
#
# smartest_students = db_manager.fetch_student_with_highest_grades()
# for smartest_student in smartest_students:
#     if smartest_student:
#         print("Student ID:", smartest_student["student_id"])
#         print("Student Name:", smartest_student["student_name"])
#         print(f"Subject: {smartest_student['subject_name']}, Grade: {smartest_student['highest_grade']}")
#         print("---")
# stupidest_students = db_manager.fetch_the_stupidest_student()
#
# for stupidest_student in stupidest_students:
#     if stupidest_student:
#         print("Student ID:", stupidest_student["student_id"])
#         print("Student Name:", stupidest_student["student_name"])
#         print(f"Subject: {stupidest_student['subject_name']}, Grade: {stupidest_student['lowest_grade']}")
#         print("---")
#
# # Закрытие соединения с базой данных
# db_manager.close()


# for students in range(1, 9):
#     medal = Medal(8, students, random.choice(["gold", "silver", "bronze", "None"]))
#     medal.save_to_database(db_manager)

student_id_to_query = 3
medals_info = db_manager.fetch_medals_by_student(student_id_to_query)
if medals_info is not None:
    print(medals_info)
# ajghkjhasgkhja