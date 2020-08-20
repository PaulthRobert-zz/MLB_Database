USE [MLB]

--Pitcher Batter Matchup
SELECT 
	DISTINCT
	P.[gameId],
--	ROW_NUMBER() OVER(PARTITION BY P.[gameId], P.[pitcherId], P.[BatterId], P.[atBatIndex] ORDER BY P.[gameId], p.[atBatIndex]) AS faceOffNumber,
	P.[pitcherId],
	P.[batterId],
	P.[atBatIndex]
INTO 
	#matchup
FROM
	[MLB].[dbo].[Pitch] P

INSERT INTO
		[MLB].[fact].[Matchup]
SELECT
	M.[gameId],
	ROW_NUMBER() OVER(PARTITION BY M.[gameId], M.[pitcherId], M.[BatterId] ORDER BY M.[gameId], M.[pitcherId], M.[atBatIndex]) AS faceOffNumber,
	M.[pitcherId],
	M.[batterId],
	M.[atBatIndex]

FROM
	#matchup M
ORDER BY
	M.[gameId],
	M.[PitcherId]

DROP TABLE #matchup

