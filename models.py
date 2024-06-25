from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///randomusergenerator.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_manager = SQLAlchemy(app)

class User(db_manager.Model):
    user_id = db_manager.Column(db_manager.Integer, primary_key=True)
    full_name = db_manager.Column(db_manager.String(100), nullable=False)
    contact_email = db_manager.Column(db_manager.String(120), unique=True, nullable=False)
    user_gender = db_manager.Column(db_manager.String(10), nullable=False)
    date_of_birth = db_manager.Column(db_manager.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.full_name}, {self.contact_email}>'

if __name__ == '__main__':
    db_manager.create_all()