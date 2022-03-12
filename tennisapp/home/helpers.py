import datetime
from .models import PlayerModel, db

# function for defining age from todays date in years
def age(dob):
    today = datetime.date.today()
    years = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        years -= 1
    return years

# function for defining losers and winners points when endpoint /game_result scoring logic
def points_logic(winner,loser):     
    losing_player = PlayerModel.query.filter_by(player_name=loser).first()
    points_deducted = losing_player.points * 0.1    
    losing_player.points = losing_player.points - points_deducted
    winning_player = PlayerModel.query.filter_by(player_name=winner).first()
    winning_player.points = winning_player.points + points_deducted
    db.session.commit()

    return {"winner_points": winning_player.points, "loser_points":losing_player.points}