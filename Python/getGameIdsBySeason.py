# for api calls
import requests

# for date manipulation
from datetime import datetime, timedelta

# pyodbc is used for connecting to the database
import pyodbc

# pandas is used for a bunch a cool stuff i think, i don't really know. here i want to use it to read the sql query results
# define the database connection parameters
import pandas

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

#set initial parameters 
season = 2010
gameType = 'R'

# build the string to request the start and end dates for a season by game type
gameTypeDateRequestString = f"http://lookup-service-prod.mlb.com/json/named.org_game_type_date_info.bam?current_sw='Y'&sport_code='mlb'&game_type=%27{gameType}%27&season=%27{season}%27"

# get the game type dates 
gameTypeDateResponse = requests.get(gameTypeDateRequestString)

# format as json
gameTypeDateResponse = gameTypeDateResponse.json()

#Regular season only (to start with)
#initialize first and last game date for regular season
first_game_date = (gameTypeDateResponse['org_game_type_date_info']['queryResults']['row'][0]['first_game_date'])
last_game_date = (gameTypeDateResponse['org_game_type_date_info']['queryResults']['row'][0]['last_game_date'])

print(f"first_game_date {first_game_date}")
print(f"last_game_date {last_game_date}")

# convert the string returned by the api to a date time value
first_game_date = datetime.strptime(first_game_date,'%Y-%m-%dT%H:%M:%S')
last_game_date = datetime.strptime(last_game_date,'%Y-%m-%dT%H:%M:%S')

# calculate the difference between start and end date
delta = last_game_date - first_game_date

print(delta)

try:
    # iterate through each date in the range
    for i in range(delta.days + 1):
        gameDate = (first_game_date + timedelta(days = i))
        # convert date to datestring in mm/dd/yyy format
        gameDate = gameDate.strftime("%m/%d/%Y")
        # build request string
        scheduleRequestString = f"http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date={gameDate}"
        # for the mlb schedule on a given date http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date=04/10/2018
        schedule = requests.get(scheduleRequestString)
        # convert to json
        schedule=schedule.json()
        # get the total number of games played that day 
        if schedule['totalGames']>0:
            for game in schedule['dates'][0]['games']:
                gameId = (game['gamePk'])

                #build sql statement
                SqlInsertStatement = ("INSERT INTO [MLB].[dbo].[Game]"
                "(gameId, gameType, season, gameDate)"
                f'VALUES ({gameId},\'{gameType}\', {season}, \'{gameDate}\')')

                #print(SqlInsertStatement)
                
                #insert a record
                cursor.execute(SqlInsertStatement)

                #without this it doesnt commit - giving you a chance to check the execution and confirm it worked,. Your can query before commit
                conn.commit()

except KeyError:
    #if there is a key error - if the key isn't present, dont push to db
    print('Error', sys.exc_info()[0])
# TO DO - use this loop to call and return the api to get the schedule and then commit it to the database
