from ..connection import get_connection

def create_workout_error(workout_id, timestamp, error_type):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into WorkoutErrors(WorkoutID, Timestamp, ErrorType) values (?, ?, ?)
    """, (workout_id, timestamp, error_type))

    connection.commit()

    cursor.close()
    connection.close()


def get_all_workout_errors():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select ErrorID, WorkoutID, Timestamp, ErrorType from WorkoutErrors
    """)

    workot_errors =  cursor.fetchall()

    cursor.close()
    connection.close()

    return workot_errors


def get_workout_error_by_error_id(error_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
            select ErrorID, WorkoutID, Timestamp, ErrorType from WorkoutErrors where ErrorID = ?
        """, (error_id,))

    workot_error = cursor.fetchone()

    cursor.close()
    connection.close()

    return workot_error


def get_workout_error_by_workout_id(workout_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
            select ErrorID, WorkoutID, Timestamp, ErrorType from WorkoutErrors where WorkoutID = ?
        """, (workout_id,))

    workot_error = cursor.fetchone()

    cursor.close()
    connection.close()

    return workot_error