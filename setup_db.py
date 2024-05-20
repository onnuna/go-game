import mysql.connector
from mysql.connector import Error

def execute_sql_script(filename):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )

        cursor = connection.cursor()
        with open(filename, 'r') as file:
            sql_script = file.read()

        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        connection.commit()
        print("Skrypt SQL został pomyślnie wykonany.")
    except Error as e:
        print(f"Błąd podczas wykonywania skryptu SQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    execute_sql_script('database/db_setup.sql')
