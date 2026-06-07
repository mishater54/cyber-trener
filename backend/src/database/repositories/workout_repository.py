from ..connection import get_connection


def create_workout(user_id, exercise_id, start_time, total_reps, success_reps, average_accurancy):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into Workouts(UserID, ExerciseID, StartTime, TotalReps, SuccessReps, AverageAccurancy) values (?, ?, ?, ?, ?, ?)
    """, (user_id, exercise_id, start_time, total_reps, success_reps, average_accurancy))

    connection.commit()

    cursor.close()
    connection.close()


def get_all_workouts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select WorkoutID, UserID, ExerciseID, StartTime, TotalReps, SuccessReps, AverageAccurancy
        from Workouts
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


def get_workout_by_id(workout_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select WorkoutID, UserID, ExerciseID, StartTime, TotalReps, SuccessReps, AverageAccurancy
        from Workouts where WorkoutID=?
    """, (workout_id,))

    workout = cursor.fetchone()

    cursor.close()
    connection.close()

    return workout

def get_workout_by_exercise_id(exercise_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
            select WorkoutID, UserID, ExerciseID, StartTime, TotalReps, SuccessReps, AverageAccurancy
            from Workouts where WorkoutID=?
        """, (exercise_id,))

    workout = cursor.fetchone()

    cursor.close()
    connection.close()

    return workout