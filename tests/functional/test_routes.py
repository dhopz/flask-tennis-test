import pytest
import json
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    
    with app.app_context():
        with app.test_client() as client:
            yield client
        
def test_home_page(client):    
    response = client.get('/')
    print(response.data)
    expected = {'hello': 'world'}
    assert response.status_code == 200
    assert expected == json.loads(response.get_data(as_text=True))

def test_home_page_2(client):    
    response = client.get('/')
    print(response.data)
    expected = {'hello': 'world'}
    assert response.status_code == 200
    assert expected == json.loads(response.get_data(as_text=True))
        
# def test_handle_players(client):     
#     response = client.get('/players')
#     res = json.loads(response.data.decode('utf-8'))
#     #print(response.data, "something else")
#     print(res)
#     #print(res.message)
#     assert response.status_code == 404
#     assert res['message'] == "success"

# def test_handle_players_2():     
#     response = create_app.test_client().get('/players')
#     print(response.data, "something else")
#     print(response)
#     #assert response.status_code == 200
#     assert response.data.message == "success"

# def test_game_result(client):
#     data = {
#         "winner":"JonesJohn",
#         "loser":"AnotherTest"
#     }
        
#     response = client.post('/game_result', data=json.dumps(data))
#     res = json.loads(response.data.decode('utf-8'))
#     #print(response.data, "something else")
#     print(res)
#     #print(res.message)
#     assert response.status_code == 200
#     assert res['message'] == "success"
