USE [MLB]

CREATE TABLE [MLB].[dbo].[Pitch](
	[playId] varchar(100) NOT NULL,
	[gameId] int NOT NULL,			--6 digits long
	[pitcherId] int,				--6 digits long
	[batterId] int,
	[atBatIndex] int,
	[pitchNumber] int,	
	--details
	[isInPlay] varchar(10),
	[isStrike] varchar(10),
	[isBall] varchar(10),
	[callCode] varchar(10),
	[typeCode] varchar(10),
	--count
	[countBalls] int,
	[countStrikes] int,
	--pitchData
	[startSpeed] decimal(5,2),
	[endSpeed] decimal(5,2),
	[strikeZoneTop] decimal(5,2),
	[strikeZoneBottom] decimal(5,2),
	--pitchData coordinates
	[aY] decimal(5,2),
	[aZ] decimal(5,2),
	[pfxX] decimal(5,2),
	[pfxZ] decimal(5,2),
	[pX] decimal(5,2),
	[pZ] decimal(5,2),
	[vX0] decimal(5,2),
	[vY0] decimal(5,2),
	[vZ0] decimal(5,2),
	[x] decimal(5,2),
	[y] decimal(5,2),
	[x0] decimal(5,2),
	[y0] decimal(5,2),
	[z0] decimal(5,2),
	[aX] decimal(5,2),
	--breaks
	[breakAngle] decimal(5,2),
	[breakLength] decimal(5,2),
	[breakY] decimal(5,2),
	[spinRate] decimal(5,2),
	[spinDirection] decimal(5,2),
	[zone] int,
	[plateTime] decimal(5,2),
	--hit Data
	[launchSpeed] decimal(5,2),
	[launchAngle] decimal(5,2),
	[totalDistance] int,
	[trajectory] varchar(50),
	[hardness] varchar(50),
	[location] varchar(10),
	--hit Coordinates
	[coordX] decimal(5,2),
	[coordY] decimal(5,2),


) ON [PRIMARY]

DROP TABLE [MLB].[dbo].Pitch