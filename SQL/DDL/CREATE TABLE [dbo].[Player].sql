USE [MLB];
Go

CREATE TABLE [dbo].[Player](
	playerId INT,
	firstName NVARCHAR(50),
	lastName NVARCHAR(50),
	jersey_number INT,
	weight INT,
	height_feet INT,
	height_inches INT,
	teamId INT,
	throws NVARCHAR(3),
	bats NVARCHAR(3),
	primary_position INT

)
