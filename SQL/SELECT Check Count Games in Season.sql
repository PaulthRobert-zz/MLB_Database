DECLARE @SEASON int = 2015


SELECT
	COUNT(*)
FROM
	GAME
WHERE
	SEASON = @SEASON


SELECT
	COUNT(*)
FROM
	(
	SELECT DISTINCT
		P.gameId
	FROM
		[Pitch] P
		INNER JOIN [Game] G ON
			G.[gameId] = P.[gameId]
	WHERE
		G.[gameDate] >= DATEFROMPARTS(@SEASON,1,1)
		AND G.[gameDate] <= DATEFROMPARTS(@SEASON,12,31)
	) AS T1
