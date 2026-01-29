from database.mysql_config import get_mysql_connection

def load_data(df):
    print("Loading data into MySQL...")
    conn = get_mysql_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO students (student_id, name, age, grade, email, department)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name=VALUES(name),
        age=VALUES(age),
        grade=VALUES(grade),
        email=VALUES(email),
        department=VALUES(department)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded successfully.")
