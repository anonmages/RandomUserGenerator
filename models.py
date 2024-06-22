from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

database_uri = os.getenv('DATABASE_URL', 'sqlite:///randomusergenerator.db')

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserProfile {self.name}, {self.email}>'

if __name__ == '__main__':
    db.create_all()