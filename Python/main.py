'''
Once a game is complete, the full dataset for the game can be accessed with this api:
    https://statsapi.mlb.com/api/v1.1/game/631377/feed/live/

    https://statsapi.mlb.com/api/v1.1/game/${gameid}/feed/live/

    here is a URL for the imafe sources for team Hat logos https://www.mlbstatic.com/team-logos/team-cap-on-light/108.svg

    for the current day's schedule: http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1

    for the mlb schedule on a given date http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date=04/10/2018

    use this to get the begining and end dates for seasons GET http://lookup-service-prod.mlb.com/json/named.org_game_type_date_info.bam?current_sw='Y'&sport_code='mlb'&game_type='L'&season='2017'
    'R' - Regular Season
    'S' - Spring Training
    'E' - Exhibition
    'A' - All Star Game
    'D' - Division Series
    'F' - First Round (Wild Card)
    'L' - League Championship
    'W' - World Series
'''
# Dependencies
    # requests
    # pandas

# requests is used for calling APIs
import requests

# pyodbc is used for connecting to the database
import pyodbc

# pandas is used for a bunch a cool stuff i think, i don't really know. here i want to use it to read the sql query results
# define the database connection parameters
# import pandas

# i think i need this one so that i can output the error messages in try catch
import sys

# INITIALIZE SQL STUFF

# define the database connection parameters
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=1S343Z2;'
    'Database=MLB;'
    'Trusted_Connection=yes;'
    )
# initialize cursor
cursor = conn.cursor()

# build select statement
selectGameId = f'SELECT G.[gameId] FROM [MLB].[dbo].[Game] G WHERE G.[season]<2019 AND G.[season]>=2010 AND G.[gameId] = 490849'
# execute the sql statement
games = cursor.execute(selectGameId)
# get all rows from the sql return value
games = games.fetchall()

# itereate over the rows returned
for game in games:  
    #build game feed request string - the wierd syntax on game is because game is a pyodbc.Row type, so the [0] index returns just the first column in the row (even tho there is only one column)
    gameFeedRequest = f'https://statsapi.mlb.com/api/v1.1/game/{game[0]}/feed/live/'

    # Get the records from the api
    # get the full JSON data for a complete MLB game
    gameFeed = requests.get(gameFeedRequest)

    #print(gameFeedRequest)
    
    #convert the response to json
    gameFeed = gameFeed.json()
    
    #Use gameFeed['liveData']['plays']['allPlays']['pitchIndex'] to iterate through the pitches
    print(gameFeed['gamePk'])
    # assign gameId outside the loop
    gameId                          = gameFeed['gamePk']

    # loop through all the plays in the game
    for play in gameFeed['liveData']['plays']['allPlays']:
        try:
            pitcherId               = play['matchup']['pitcher']['id'] 
            batterId                = play['matchup']['batter']['id']
            atBatIndex              = play['atBatIndex']
            # #loop through all the play events in each play node
            for playEvent in play['playEvents']:
                playId              = playEvent['playId']
                # details
                isInPlay            = playEvent['details']['isInPlay']
                isStrike            = playEvent['details']['isStrike']
                isBall              = playEvent['details']['isBall']
                callCode            = playEvent['details']['call']['code']
                typeCode            = playEvent['details']['type']['code']
                # count
                countBalls          = playEvent['count']['balls']
                countStrikes        = playEvent['count']['strikes']
                # pitchData
                startSpeed          = playEvent['pitchData']['startSpeed']
                endSpeed            = playEvent['pitchData']['endSpeed']
                strikeZoneTop       = playEvent['pitchData']['strikeZoneTop']
                strikeZoneBottom    = playEvent['pitchData']['strikeZoneBottom']
                # pitchData coordinates
                aY                  = playEvent['pitchData']['coordinates']['aY']
                aZ                  = playEvent['pitchData']['coordinates']['aZ']
                pfxX                = playEvent['pitchData']['coordinates']['pfxX']
                pfxZ                = playEvent['pitchData']['coordinates']['pfxZ']
                pX                  = playEvent['pitchData']['coordinates']['pX']
                pZ                  = playEvent['pitchData']['coordinates']['pZ']
                vX0                 = playEvent['pitchData']['coordinates']['vX0']
                vY0                 = playEvent['pitchData']['coordinates']['vY0']
                vZ0                 = playEvent['pitchData']['coordinates']['vZ0']
                x                   = playEvent['pitchData']['coordinates']['x'] 
                y                   = playEvent['pitchData']['coordinates']['y']
                x0                  = playEvent['pitchData']['coordinates']['x0']
                y0                  = playEvent['pitchData']['coordinates']['y0']
                z0                  = playEvent['pitchData']['coordinates']['z0']
                aX                  = playEvent['pitchData']['coordinates']['aX']
                # breaks
                # LOOKOUT SOME OF THESE ELEMENTS ARE NOT PRESENT SOME TIME 
                # You are going to need to check for the presence of the element
                breakAngle          = playEvent['pitchData']['breaks']['breakAngle']
    
                # #these arent present on the data set i am working with today - maybe they vary by ball park - depending on the equipment??
                # # breakLength         = playEvent['pitchData']['breaks']['breakLength']
                # # breakY              = playEvent['pitchData']['breaks']['breakY']
                # # spinRate            = playEvent['pitchData']['breaks']['spinRate']
                # # spinDirection       = playEvent['pitchData']['breaks']['spinDirection']
                # # zone                = playEvent['pitchData']['breaks']['zone']
                # # plateTime           = playEvent['pitchData']['breaks']['plateTime']
                
                # # hit data 
                # # #Check for the hit data node with a try catch
                try:
                    launchSpeed         = playEvent['hitData']['launchSpeed']
                    launchAngle         = playEvent['hitData']['launchAngle']
                    totalDistance       = playEvent['hitData']['totalDistance']
                    trajectory          = playEvent['hitData']['trajectory']
                    hardness            = playEvent['hitData']['hardness']
                    location            = playEvent['hitData']['location']
                    # hit coordinates 
                    coordX              = playEvent['hitData']['coordinates']['coordX']
                    coordY              = playEvent['hitData']['coordinates']['coordY']
                    pitchNumber         = playEvent['pitchNumber']
                except KeyError:
                    launchSpeed         = 0
                    launchAngle         = 0
                    totalDistance       = 0
                    trajectory          = 0
                    hardness            = 0
                    location            = 0
                    # hit coordinates 
                    coordX              = 0
                    coordY              = 0
                    pitchNumber         = 0
                
                # print(f"playId {playId}")   
                # print(f"gameId {gameId}")
                # print(f"pitcherId {pitcherId}")
                # print(f"batterId {batterId}")
                
                # # details
                # print(f"isInPlay {isInPlay}")
                # print(f"isStrike {isStrike}")
                # print(f"isBall {isBall}")
                # print(f"callCode {callCode}")
                # print(f"typeCode {typeCode}")

                # # count
                # print(f"countBalls {countBalls}")
                # print(f"countStrikes {countStrikes}")

                # # pitchData
                # print(f"startSpeed {startSpeed}")
                # print(f"endSpeed {endSpeed}")
                # print(f"strikeZoneTop {strikeZoneTop}")
                # print(f"strikeZoneBottom {strikeZoneBottom}")

                # # coordinates
                # print(f"aY {aY}")
                # print(f"aZ {aZ}")
                # print(f"pfxX {pfxX}")
                # print(f"pfxZ {pfxZ}")
                # print(f"pX {pX}")
                # print(f"pZ {pZ}")
                # print(f"vX0 {vX0}")
                # print(f"vY0 {vY0}")
                # print(f"vZ0 {vZ0}")
                # print(f"x {x}")
                # print(f"y {y}")
                # print(f"x0 {x0}")
                # print(f"y0 {y0}")
                # print(f"z0 {z0}")
                # print(f"aX {aX}")

                # # breaks
                # print(f"breakAngle {breakAngle}")
                
                # #hit data 
                # print(f"launchSpeed {launchSpeed}")
                # print(f"launchAngle {launchAngle}")
                # print(f"totalDistance {totalDistance}")
                # print(f"trajectory {trajectory}")
                # print(f"hardness {hardness}")
                # print(f"location {location}")

                # # hit coordinates 
                # print(f"coordX {coordX}")
                # print(f"coordY {coordY}")
                # print(f"pitchNumber {pitchNumber}")
                # print(f"atBatIndex {atBatIndex}")

                #build sql statement
                SqlInsertStatement = ("INSERT INTO [MLB].[dbo].[Pitch]"
                "(playId, gameId, pitcherId, batterId, isInPlay, isStrike, isBall, callCode, typeCode, countBalls, countStrikes, startSpeed, endSpeed, strikeZoneTop, strikeZoneBottom, aY, aZ, pfxX, pfxZ, pX, pZ, vX0, vY0, vZ0, x, y, x0, y0, z0, aX, breakAngle, launchSpeed, launchAngle, totalDistance, trajectory, hardness, location, coordX, coordY, pitchNumber, atBatIndex)"
                f'VALUES (\'{playId}\',{gameId},{pitcherId},{batterId},\'{isInPlay}\',\'{isStrike}\',\'{isBall}\',\'{callCode}\',\'{typeCode}\',{countBalls},{countStrikes},{startSpeed},{endSpeed},{strikeZoneTop},{strikeZoneBottom},{aY},{aZ},{pfxX},{pfxZ},{pX},{pZ},{vX0},{vY0},{vZ0},{x},{y},{x0},{y0},{z0},{aX},{breakAngle},{launchSpeed},{launchAngle},{totalDistance},\'{trajectory}\',\'{hardness}\',{location},{coordX},{coordY},{pitchNumber},{atBatIndex})')


                # print(SqlInsertStatement)
                
                #insert a record
                cursor.execute(SqlInsertStatement)

                # #without this it doesnt commit - giving you a chance to check the execution and confirm it worked,. Your can query before commit
                conn.commit()

        except KeyError:
            #if there is a key error - if the key isn't present, dont push to db
            print('Error', sys.exc_info()[0])