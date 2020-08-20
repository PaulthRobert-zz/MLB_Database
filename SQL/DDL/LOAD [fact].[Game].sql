
--TRUNCATE TABLE [fact].[Game]
INSERT INTO 
	[MLB].[fact].[Game]

SELECT
	G.[gameId],
	G.[gameDate],
	NULL AS homeTeamId,
	NULL AS awayTeamID,
	MAX(P.[atBatIndex]) AS totalPlateAppearances,
	COUNT(P.[playId]) AS totalPitches --**NOTE* if any of these plays are not pitch plays (like how is a pick off attempt logged?) it will throw off the count
FROM
	[MLB].[dbo].[Game] G

	LEFT JOIN [MLB].[dbo].[Pitch] P ON
		P.gameId = G.[gameId]
GROUP BY
	G.[gameId],
	G.[gameDate]


SELECT
	*
FROM
	[fact].[Game]