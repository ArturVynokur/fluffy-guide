import mysql.connector


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def fetch_student_by_id(self, student_id):
        query = """
        SELECT students.student_id, students.student_name, grades.grade, subjects.subject_name
        FROM students
        LEFT JOIN grades ON students.student_id = grades.student_id
        LEFT JOIN subjects ON grades.subject_id = subjects.subject_id
        WHERE students.student_id = %s
        """
        value = (student_id,)
        self.cursor.execute(query, value)
        result = self.cursor.fetchall()
        if not result:
            return None
        student_info = {
            "student_id": result[0][0],
            "student_name": result[0][1],
            "grades": []
        }
        for row in result:
            if row[2] is not None:
                student_info["grades"].append({
                    "grade": row[2],
                    "subject": row[3]
                })
        return student_info

    def fetch_excellent_students(self, threshold):
        query = """
            SELECT students.student_id, students.student_name, grades.grade, subjects.subject_name
            FROM students
            LEFT JOIN grades ON students.student_id = grades.student_id
            LEFT JOIN subjects ON grades.subject_id = subjects.subject_id
            WHERE grades.grade >= %s
            GROUP BY students.student_id
            HAVING COUNT(grades.grade) = SUM(IF(grades.grade >= %s, 1, 0))
        """
        values = (threshold, threshold)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()

        excellent_students = []

        for row in result:
            student_info = {
                "student_id": row[0],
                "student_name": row[1],
                "grades": [{
                    "subject": row[3],
                    "grade": row[2]
                }]
            }
            excellent_students.append(student_info)

        return excellent_students

    def fetch_student_with_highest_grades(self):
        query = """
              SELECT students.student_id, students.student_name, subjects.subject_name,
              MAX(grades.grade) as highest_grade
              FROM students
              JOIN grades ON students.student_id = grades.student_id
              JOIN subjects ON grades.subject_id = subjects.subject_id
              GROUP BY students.student_id, subjects.subject_name
              ORDER BY highest_grade DESC
              LIMIT 1
          """
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        students_with_highest_grades = []

        for row in result:
            student_info = {
                "student_id": row[0],
                "student_name": row[1],
                "subject_name": row[3],
                "highest_grade": row[2]
            }
            students_with_highest_grades.append(student_info)

        return students_with_highest_grades

    def fetch_the_stupidest_student(self):
        query = """
            SELECT students.student_id, students.student_name, subjects.subject_name,
            MIN(grades.grade) as lowest_grade
            FROM students
            LEFT JOIN grades ON students.student_id = grades.student_id
            LEFT JOIN subjects ON grades.subject_id = subjects.subject_id
            GROUP BY students.student_id, subjects.subject_name
            ORDER BY lowest_grade ASC
            LIMIT 1
          """

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        the_stupidest_student = []

        for row in result:
            student_info = {
                "student_id": row[0],
                "student_name": row[1],
                "subject_name": row[3],
                "lowest_grade": row[2]
            }
            the_stupidest_student.append(student_info)

        return the_stupidest_student

    def fetch_medals_by_student(self, student_id):
        if not None:
            query = """
            SELECT students.student_id, students.student_name, medals.medal_type, 
            GROUP_CONCAT(subjects.subject_name) AS subject_names
            FROM students 
            LEFT JOIN medals ON students.student_id = medals.student_id
            LEFT JOIN subjects ON medals.subject_id = subjects.subject_id
            WHERE medals.student_id = %s
            GROUP BY medals.student_id, medals.medal_type
            """
            value = (student_id,)
            self.cursor.execute(query, value)
            result = self.cursor.fetchall()

            student_data = {}

            for row in result:
                if row is not None:
                    student_id, student_name, medal_type, subject_name = row
                    if student_id not in student_data:
                        student_data[student_id] = {
                            'name': student_name,
                            'medals': []
                        }
                    student_data[student_id]['medals'].append((medal_type, subject_name))

            for student_id, data in student_data.items():
                print(f"Имя {data['name']}")
                for medal_type, subject_names in data['medals']:
                    if subject_names is not None:
                        print(f"{len(subject_names.split(','))} {medal_type} ({subject_names})")
