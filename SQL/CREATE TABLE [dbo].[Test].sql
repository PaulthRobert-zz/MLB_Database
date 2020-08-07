USE [MLB]

CREATE TABLE [MLB].[dbo].[Test](

	CatID int IDENTITY(1,1) NOT NULL, --This is a way of creating a primary key in tables
	Name varchar(50) NOT NULL,
	DateOfBirth date NULL
) ON [PRIMARY] -- this has something to do with where the data is stored - file group