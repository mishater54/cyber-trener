import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Creates and returns a connection to the database
    """

    driver = os.getenv("DB_DRIVER")
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password};"
        f"TrustServerCertificate=yes;"
    )

    try:
        return pyodbc.connect(connection_string)

    except pyodbc.Error as error:
        raise ConnectionError(f"Database connection failed: {error}")

def test_connection():
    """
    Checks if the connection to the database is working
    """

    try:
        connection = get_connection()
        print("Database connection established")
        connection.close()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_connection()