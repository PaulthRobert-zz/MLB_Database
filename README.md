# MLB_Database
Py proj to build a killer mlb db

What to do next?

Adding a comment to test git. 

Script the database build from scratch to data load and validation
    - build the validation part
        1) Load Game Data for 1 Season
        2) Load Pitch Data for that Season
        3) Extract the unique list of gameIDs from the Game Data
        4) Extract the unique list of gameIDs from the Pitch Data
        5) Report Out which games are missing.
            The Issue 2019 Test

            There are 
                2,578 Regular Season games in [dbo].[Game]
                2,436 games in [dbo].[Pitch]
                142 games missing

                When Inner Joined, there are 2,475

        6) Use this comparison to do something useful - which games are missing, try to re-fetch?


        Other Nice to Haves:
        - log the key errors differently?
        - time meta data metrics? 
          - how long does it take to pull the records for a season
          - Incorperate non regular season games


    Bring in Dimentions
        Player
            id
            name
            number
            position

        Team Names
            id
            name
            league
            division

        Venue Names
        Pitch Type Names
