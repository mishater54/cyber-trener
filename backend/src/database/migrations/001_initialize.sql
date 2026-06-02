USE cyber_trainer
GO

CREATE TABLE dbo.Exercises(
    ExerciseID INT IDENTITY(1,1),
    ExerciseName NVARCHAR(50),
    Description NVARCHAR(MAX)
)
GO

CREATE TABLE dbo.Users(
    UserID INT IDENTITY(1,1),
    FullName NVARCHAR(100),
    Email NVARCHAR(100),
    CreatedAt DATETIME DEFAULT GETDATE()
)
GO

CREATE TABLE dbo.Workouts(
    WorkoutID INT IDENTITY(1,1),
    UserID INT,
    ExerciseID INT,
    StartTime DATETIME DEFAULT GETDATE(),
    TotalReps INT,
    SuccessReps INT,
    AverageAccuracy FLOAT
)
GO

CREATE TABLE dbo.WorkoutErrors(
    ErrorID INT IDENTITY(1,1),
    WorkoutID INT,
    TimeStamp TIME(7),
    ErrorType NVARCHAR(255)
)
GO