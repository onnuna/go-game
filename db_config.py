import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="go_game_db"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Błąd podczas łączenia z bazą danych: {e}")
    return None

def close_db_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")

def execute_query(query, params=None):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor
        except Error as e:
            print(f"Błąd podczas wykonywania zapytania: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_db_connection(connection)
    return None

def fetch_results(query, params=None):
    cursor = execute_query(query, params)
    if cursor:
        results = cursor.fetchall()
        cursor.close()
        return results
    return None
