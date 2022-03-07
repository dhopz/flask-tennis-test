from tennisapp.models import PlayerModel

def test_new_player():
    ''' 
    GIVEN a Player Model
    WHEN a new Player is created
    THEN check data is in correct format
    '''
    player = PlayerModel("Player1","McTest","British","14/01/2000")
    assert player.first_name == "Player1"
    assert player.last_name == "McTest"
    assert player.nationality == "British"
    assert player.date_of_birth == "14/01/2000"
    assert player.points == "1200"
