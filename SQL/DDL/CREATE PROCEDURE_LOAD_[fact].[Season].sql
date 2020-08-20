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
CREATE PROCEDURE [dbo].[LOAD_fact.Season]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    TRUNCATE TABLE [fact].[Season]
	INSERT INTO 
	[MLB].[fact].[Season]
	SELECT DISTINCT
		G.[Season],
		G.[gameType],
		COUNT(G.[gameId]) OVER (PARTITION BY G.[season], G.[gameType]) AS [gameCount]

	FROM
		Game [G]	

	ORDER BY G.[Season]
END
GO


