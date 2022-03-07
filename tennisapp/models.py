from . import db

class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    nationality = db.Column(db.String())
    date_of_birth = db.Column(db.Date())
    points = db.Column(db.Integer(),default=1200)
    __table_args__ = (db.UniqueConstraint('last_name', 'first_name', name='player_name_uc'),)
    #player_name = db.column(db.String(),primary_key=True)

    def __init__(self, first_name, last_name, nationality, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

       