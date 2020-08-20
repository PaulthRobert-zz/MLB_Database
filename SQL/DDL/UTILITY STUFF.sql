--TRUNCATE TABLE Game
--TRUNCATE TABLE Pitch
--TRUNCATE TABLE [fact].[Season]

SELECT
	*
FROM
	Game
WHERE
	gameId = '565221'

--TRUNCATE TABLE Game
--DROP TABLE [dbo].[Game]

SELECT
	*
FROM
	Pitch
--TRUNCATE TABLE Pitch

SELECT
	*
FROM
	[fact].[Season]
--TRUNCATE TABLE [fact].[Season]

SELECT
	*
FROM
	[fact].[Game]


SELECT
	DISTINCT
	P.[gameId]
INTO 
	#game
FROM
	[dbo].[Pitch] P

SELECT
	COUNT(G.[gameId])
FROM
	#game G
DROP TABLE #game

	