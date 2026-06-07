from ..connection import get_connection




def get_all_exercises():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT ExerciseID,
                ExerciseName,
                Description
        FROM dbo.Exercises
    """)

    exercises = cursor.fetchall()

    cursor.close()
    connection.close()

    return exercises

def get_exercise_by_id(exercise_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select ExerciseID, ExerciseName, Description 
        from dbo.Exercises 
        where ExerciseID= ?""", exercise_id)

    exercise = cursor.fetchone()

    cursor.close()
    connection.close()

    return exercise


def create_exercise(name, description):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into dbo.Exercises (ExerciseName, Description)
        values (?, ?)
    """, name, description)

    connection.commit()
    cursor.close()
    connection.close()
