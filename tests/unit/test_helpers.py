from tennisapp.home.helpers import age, points_logic
import datetime

def test_age():
    age_string = "14/01/2000"
    age_calc = age(datetime.datetime.strptime(age_string, '%d/%m/%Y'))   
    assert age_calc == 22

# def test_points_logic(client):
#     game_result = points_logic("AnotherTest","AnotherTest1")
#     assert game_result == {"winner_points": 1320, "loser_points":1080}