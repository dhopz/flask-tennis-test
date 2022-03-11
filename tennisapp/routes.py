"""Application routes."""
#from datetime import datetime
import datetime
from sqlalchemy import exc
from flask import current_app as app
from flask import request, json
from init_db import session

from .models import PlayerModel, GameResultModel, db

def age(dob):
    today = datetime.date.today()
    years = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        years -= 1
    return years


@app.route('/')
def hello():
	return {"hello": "world"}

@app.route('/players', methods=['POST', 'GET'])
def handle_players():
    try:
        if request.method == 'POST':
            data = json.loads(request.data)

            if age(datetime.datetime.strptime(data['date_of_birth'], '%d/%m/%Y')) >= 16:
                new_player = PlayerModel(                
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    nationality=data['nationality'],
                    date_of_birth=datetime.datetime.strptime(data['date_of_birth'], '%d/%m/%Y'),
                    player_name=data['last_name']+data['first_name']           
                    )
                db.session.add(new_player)
                db.session.commit()
                return {"message": f"Player {new_player.first_name} {new_player.last_name} has been created successfully."}
            else:
                return {"error": "The Player needs to be at least 16"}


        elif request.method == 'GET':
            players = PlayerModel.query.all()
            results = [
                {
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "nationality": player.nationality
                } for player in players]

            return {"count": len(results), "Players": results, "message": "success"}    
    
    except exc.IntegrityError:
        return {"error": "The Player has already been registered"}

@app.route('/game_result', methods=['POST'])
def game_result():
    data = json.loads(request.data)
    winner, loser = data['winner'], data['loser']
    points_logic(winner,loser)   
    result = GameResultModel(                
                    winner=winner,
                    loser=loser,            
                    )
    db.session.add(result)
    db.session.commit()
    #winner = PlayerModel.query.filter_by(player_name=winner)
    return {"message": "Games Result recorded"}


# nationality or current rank
# for example nationality/british or current_rank/bronze
@app.route('/player_rankings/', defaults={'query_type': None, 'query_parameter': None})
@app.route('/player_rankings/<string:query_type>/<string:query_parameter>', methods=['GET'])
def player_rankings(query_type, query_parameter):
    print(query_type, query_parameter)
    if query_type == 'nationality':
        players = session.execute(f"SELECT * FROM player_rankings WHERE nationality = '{query_parameter}'").all()
    elif query_type == 'current_rank':
        players = session.execute(f"SELECT * FROM player_rankings WHERE current_rank = '{query_parameter}'").all()
    else:
        players = session.execute("SELECT * FROM player_rankings").all()
        
    results = [
        {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "nationality": player.nationality,
            "age":player.age,
            "points":player.points,
            "current_rank":player.current_rank
        } for player in players]
    
    return {"count": len(results), "Players": results, "message": "success"}    

def points_logic(winner,loser):     
    losing_player = PlayerModel.query.filter_by(player_name=loser).first()
    print(losing_player.points, "losing player points")
    points_deducted = losing_player.points * 0.1
    print(points_deducted)
    losing_player.points = losing_player.points - points_deducted

    winning_player = PlayerModel.query.filter_by(player_name=winner).first()
    winning_player.points = winning_player.points + points_deducted
    print(winning_player.points)
    db.session.commit()

    return 