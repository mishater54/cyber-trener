USE cyber_trainer
GO

ALTER TABLE dbo.Exercises
ADD CONSTRAINT PK_Exercises
PRIMARY KEY (ExerciseID)
GO

ALTER TABLE dbo.Users
ADD CONSTRAINT PK_Users
PRIMARY KEY (UserID)
GO

ALTER TABLE dbo.Workouts
ADD CONSTRAINT PK_Workouts
PRIMARY KEY (WorkoutID)
GO

ALTER TABLE dbo.WorkoutErrors
ADD CONSTRAINT PK_WorkoutErrors
PRIMARY KEY (ErrorID)
GO

ALTER TABLE dbo.Workouts
ADD CONSTRAINT FK_Workouts_Users
FOREIGN KEY (UserID)
REFERENCES dbo.Users(UserID)
GO

ALTER TABLE dbo.Workouts
ADD CONSTRAINT FK_Workouts_Exercises
FOREIGN KEY (ExerciseID)
REFERENCES dbo.Exercises(ExerciseID)
GO

ALTER TABLE dbo.WorkoutErrors
ADD CONSTRAINT FK_WorkoutErrors_Workouts
FOREIGN KEY (WorkoutID)
REFERENCES dbo.Workouts(WorkoutID)
GO