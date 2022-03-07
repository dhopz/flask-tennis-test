"""Application routes."""
#from datetime import datetime
import datetime
from sqlalchemy import exc

from flask import current_app as app
from flask import request, jsonify, json

from .models import PlayerModel, db

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
                    date_of_birth=datetime.datetime.strptime(data['date_of_birth'], '%d/%m/%Y')            
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
                    "nationality": player.nationality,
                    "date_of_birth":player.date_of_birth
                } for player in players]

            return {"count": len(results), "Players": results, "message": "success"}    
    
    except exc.IntegrityError:
        return {"error": "The Player has already been registered"}