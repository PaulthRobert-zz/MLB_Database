USE [MLB]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Author:		<Paul Davis>
-- Create date: <08/20/20>
-- Description:	<Loads the season table with fact values>
-- =============================================

--ALTER PROCEDURE [dbo].[LOAD_fact.PitcherSeason]
--	-- Add the parameters for the stored procedure here
--AS
--BEGIN
--	-- SET NOCOUNT ON added to prevent extra result sets from
--	-- interfering with SELECT statements.
--	SET NOCOUNT ON;

--    TRUNCATE TABLE [fact].[Season]
--	INSERT INTO 
--	[MLB].[fact].[Season]

	SELECT
		  PIT.[playerId]
		, PIT.[firstName] AS [PitcherFirstName]
		, PIT.[lastName] AS [PitcherLastName]
		, PA.[pitchHand]
		, G.[season]
		,PA.[GameId]
		,G.[homeTeam]
		,HT.[name]
		,G.[awayTeam]
		,AT.[name]
		,PA.[halfInning]
		,PA.[atBatIndex]
		,PA.[batterId]	
		,BAT.[firstName] AS [BatterFirstName]
		,BAT.[lastName] AS [BatterLastName]
		,PA.[batSide]


		--,PA.*
	--G    - Games
	--	Sum of games where pitches thrown> 0

	--GS   - Games Started
	--	Sum of games where atBatIntex 0 pitcherId = @pitcherId

	--IP   - Innings Pitched
	--	Count of innings where pitchesThrown > 0
	FROM
		[MLB].[dbo].[Player] PIT -- Pitcher

		LEFT JOIN [MLB].[dbo].[PlateAppearance] PA ON PIT.[playerId] = PA.[pitcherId]

		LEFT JOIN [MLB].[dbo].[Game] G ON PA.[GameId] = G.[gameId]

		LEFT JOIN [MLB].[dbo].[Player] BAT ON PA.[batterId] = BAT.[playerId]

		LEFT JOIN [MLB].[dbo].[Team] HT ON G.[homeTeam] = HT.[teamId]
		
		LEFT JOIN [MLB].[dbo].[Team] AT ON G.[awayTeam] = AT.teamId

		

	WHERE
		PIT.[primaryPosition] = '1' -- player is a pitcher

		--TEST
		--AND P.[playerId] = '592332'
		--AND G.[gameId] = '567112'
	ORDER BY 
		PIT.[playerId]
		,PA.[GameId]	
		,PA.[atBatIndex]

	
--END
--GO


