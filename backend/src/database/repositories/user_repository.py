from ..connection import get_connection


def create_user(full_name, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into Users(FullName,Email) values (?,?)
    """, (full_name, email))

    connection.commit()

    cursor.close()
    connection.close()


def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select UserID, FullName, Email, CreatedAt from Users
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select UserID, FullName, Email, CreatedAt from Users where UserID = ?
    """, (user_id,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def get_user_by_email(email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select UserID, FullName, Email, CreatedAt from Users where Email = ?
    """, (email,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user