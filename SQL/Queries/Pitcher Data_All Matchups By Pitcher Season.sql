/*
Write a sp that lets you pass 
	PlayerId Pitcher (pitchers only)
	GameId

	Return 


	For any given pitcher i want to know

	Pitcher Career Stats Summary
														-- Season '21 --	--Season '20 --		-- Season '19 --	-- Career --
		G    - Games
		GS   - Games Started
		IP   - Innings Pitched

		K/9  - Strikeouts per 9 innings
		BB/9 - Walks per 9 innings
		K/BB - Strikeout to Walk Ratio
		HR/9 - Home Runs  per 9 innings
		K%   - Strikeout Percentage
		BB%  - Walk Percentage
		K%-BB% - Strikout Percentage - Walk Percentage
		WHIP - Walks Plus Hits per Inning Pitched

		BABIP - Batting Average on Balls in Play


	Pitcher Profile
		Hand - 
		G    - Games
		GS   - Games Started
		IP   - Innings Pitched

		Pitch Count
			Average
		
		Pitches								-- vs. LHB --		-- vs. RHB --
			Type - frequency (count) | % 

*/

/*
	Test Params
	pitcherId = 592332 Kevin	Gausman
*/

DECLARE
	@pitcherId INT = '592332'
	, @season INT = 2020

SELECT
	*
FROM
	[MLB].[dbo].[PlateAppearance] PA

	INNER JOIN [MLB].[dbo].[Game] G ON PA.[GameId] = G.[gameId]

WHERE
	G.detailedState NOT IN('Postponed') --exludes any postponed or other 
	AND PA.[pitcherId] = @pitcherId
	AND G.season = @season

ORDER BY
	PA.[GameId]
	,PA.[atBatIndex]