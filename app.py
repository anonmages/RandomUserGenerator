from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///randomusergenerator.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)

from flask import Blueprint

random_user_bp = Blueprint('random_user', __name__)

@random_register_bp.route('/generate_user', methods=['GET'])
def generate_user():
    return "Random User"

app.register_blueprint(random_user_bp, url_prefix='/random_user')

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_debug', True))