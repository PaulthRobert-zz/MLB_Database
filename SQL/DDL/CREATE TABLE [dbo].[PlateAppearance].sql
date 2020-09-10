USE [MLB]
DROP TABLE [MLB].[dbo].[PlateAppearance]
CREATE TABLE [MLB].[dbo].[PlateAppearance](
	[GameId] INT,
	[halfInning] NVARCHAR(7),
	[inning] INT,
	[atBatIndex] INT,
	[pitcherId] INT,
	[pitchHand] NVARCHAR(2),
	[batterId] INT,
	[batSide] NVARCHAR(2),
	[startTime] DATETIME,
	[endTime] DATETIME,
	[isScoringPlay] NVARCHAR(6),
	[resultType] NVARCHAR(25),
	[event] NVARCHAR(25),
	[eventType] NVARCHAR(25),
	[rbi] INT,
	[awayScore] INT,
	[homeScore] INT

) ON [PRIMARY]