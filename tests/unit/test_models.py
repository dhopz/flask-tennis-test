from tennisapp.home.models import GameResultModel, PlayerModel

def test_new_player():
    ''' 
    GIVEN a Player Model
    WHEN a new Player is created
    THEN check data is in correct format
    '''
    player = PlayerModel("McTestPlayer1","Player1","McTest","British","14/01/2000")
    assert player.player_name == "McTestPlayer1"
    assert player.first_name == "Player1"
    assert player.last_name == "McTest"
    assert player.nationality == "British"
    assert player.date_of_birth == "14/01/2000"

def test_game_result():
    game_result = GameResultModel("TestPlayer","TestPlayer1")
    assert game_result.winner == "TestPlayer"
    assert game_result.loser == "TestPlayer1"