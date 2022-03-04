from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/tennis"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class PlayerModel(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    nationality = db.Column(db.String())
    date_of_birth = db.Column(db.DateTime())

    def __init__(self, first_name, last_name, nationality, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"<Player {self.first_name} {self.last_name}>"

@app.route('/')
def hello():
	return {"hello": "world"}