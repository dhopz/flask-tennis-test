import pytest
import json
import datetime
from app import create_app
from tennisapp import db
from tennisapp.home.models import PlayerModel

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    
    with app.app_context():
        db.create_all()
        player1 = PlayerModel("AnotherTest","Test","Another","British",datetime.date(2000, 1, 14))
        player2 = PlayerModel("JonesJohn","Jones","John","British",datetime.date(2000, 1, 14))
        
        players = [player1, player2]

        for player in players:
            db.session.add(player)
            db.session.commit()
        
        with app.test_client() as client:
            yield client
        
def test_connection(client):    
    response = client.get('/')
    expected = {'hello': 'world'}
    assert response.status_code == 200
    assert expected == json.loads(response.get_data(as_text=True))
       
def test_get_all_players(client):     
    response = client.get('/players')
    res = json.loads(response.data.decode('utf-8'))    
    assert response.status_code == 200
    assert res['message'] == "success"

def test_player_over_16(client):
    data = {
        "first_name":"Jack",
        "last_name":"Yojimbo",
        "nationality":"France",
        "date_of_birth":"14/01/2010"
    }
    response = client.post('/players', data=json.dumps(data))
    res = json.loads(response.data.decode('utf-8'))    
    assert res['error'] == "The Player needs to be at least 16"

def test_create_player(client):
    data = {
        "first_name":"John",
        "last_name":"Jones",
        "nationality":"British",
        "date_of_birth":"14/01/2000"
    }
    response = client.post('/players', data=json.dumps(data))
    res = json.loads(response.data.decode('utf-8'))
    print(res)
    assert res['message'] == "Player John Jones has been created successfully."

def test_duplicate_player(client):
    data = {
        "first_name":"John",
        "last_name":"Jones",
        "nationality":"British",
        "date_of_birth":"14/01/2000"
    }
    response = client.post('/players', data=json.dumps(data))
    response2 = client.post('/players', data=json.dumps(data))
    res = json.loads(response2.data.decode('utf-8'))
    print(res)
    assert res['error'] == "The Player has already been registered"
    
def test_game_result(client):
    data = {
        "winner":"AnotherTest",
        "loser":"JonesJohn"
    }       
    response = client.post('/game_result', data=json.dumps(data))
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert res['message'] == "Games Result recorded"
    assert res['scoring_logic'] == {'loser_points': 1080, 'winner_points': 1320}

def test_player_rankings(client):
    response = client.get('/player_rankings/')
    res = json.loads(response.data.decode('utf-8')) 
    print(res)   
    assert response.status_code == 200
    assert res['message'] == "success"