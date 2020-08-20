--Pitcher Batter Matchups


SELECT
	P.[gameId],
	ROW_NUMBER() OVER(PARTITION BY P.[pitcherId], P.[BatterId], P.[atBatIndex] ORDER BY p.[atBatIndex]) AS faceOffNumber,
	P.[pitcherId],
	P.[batterId],
	P.[atBatIndex]
FROM
	[MLB].[dbo].[Pitch] P