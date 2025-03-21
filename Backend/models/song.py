from models import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    artist = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist
        }
