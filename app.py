from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['DB_URI'] = os.getenv('DATABASE_URI', 'sqlite:///random_user_gen.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)

random_user_blueprint = Blueprint('random_user_bp', __name__)

@random_user_blueprint.route('/generate', methods=['GET'])
def generate_random_user():
    return "Random User Generated"

app.register_blueprint(random_user_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', True))