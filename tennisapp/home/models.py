from tennisapp import db
from sqlalchemy_views import CreateView
from sqlalchemy import Table, MetaData
from sqlalchemy.sql import text
from sqlalchemy_utils import create_view

class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    nationality = db.Column(db.String())
    date_of_birth = db.Column(db.Date())
    points = db.Column(db.Integer(),default=1200)
    player_name = db.Column(db.String())
    __table_args__ = (db.UniqueConstraint('last_name', 'first_name', name='player_name_uc'),)
    

    def __init__(self, player_name, first_name, last_name, nationality, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.player_name = player_name

class GameResultModel(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer,primary_key=True)
    winner = db.Column(db.String())
    loser = db.Column(db.String())

    def __init__(self,winner,loser):
        self.winner = winner
        self.loser = loser



       