from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')

engine = create_engine("postgresql+psycopg2://"+DATABASE_USERNAME+":postgres@localhost/tennis")

# Initialize the session
session = Session(engine)
query = """
CREATE OR REPLACE VIEW games_won AS
SELECT COUNT(winner) AS games, winner AS player
FROM result
GROUP BY player;

CREATE OR REPLACE VIEW games_lost AS
SELECT COUNT(loser) AS games, loser AS player
FROM result
GROUP BY player;

CREATE OR REPLACE VIEW games_played AS
SELECT SUM(games) AS games, player FROM
(SELECT * FROM games_lost
UNION
SELECT * FROM games_won) AS total_games
GROUP BY player;

CREATE OR REPLACE VIEW player_rank AS
SELECT first_name, last_name, EXTRACT(YEAR from AGE(CURRENT_DATE, date_of_birth)) as "age", nationality, points,
    CASE
        WHEN games_played.games IS NULL THEN 'Unranked'
        WHEN games_played.games < 3 THEN 'Unranked'
        WHEN points BETWEEN 0 AND 2999 THEN 'Bronze'
        WHEN points BETWEEN 3000 AND 4999 THEN 'Silver'
        WHEN points BETWEEN 5000 AND 9999 THEN 'Gold'
        WHEN points >= 10000 THEN 'Supersonic Legend'
    END AS current_rank
FROM players
LEFT JOIN games_played
    ON games_played.player = players.player_name;

CREATE OR REPLACE VIEW player_rankings AS
SELECT first_name, last_name, age, nationality, points, current_rank
FROM player_rank
ORDER BY
    CASE 
        WHEN current_rank = 'Unranked' THEN 5
        WHEN current_rank = 'Bronze' THEN 4
        WHEN current_rank = 'Silver' THEN 3
        WHEN current_rank = 'Gold' THEN 2
        WHEN current_rank = 'Supersonic Legend' THEN 1
    END;
"""

session.execute(query)
session.commit()