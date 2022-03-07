"""Application routes."""
from datetime import datetime

from flask import current_app as app
from flask import request, jsonify, json

from .models import PlayerModel, db

@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/players', methods=['POST', 'GET'])
def handle_players():
    if request.method == 'POST':
        data = json.loads(request.data)        
        new_player = PlayerModel(                
            first_name=data['first_name'],
            last_name=data['last_name'],
            nationality=data['nationality'],
            date_of_birth=datetime.strptime(data['date_of_birth'], '%d/%m/%Y')            
            )

        db.session.add(new_player)
        db.session.commit()

        return {"message": f"Player {new_player.first_name} {new_player.last_name} has been created successfully."}

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