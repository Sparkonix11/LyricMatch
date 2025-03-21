from flask_restful import Resource
from models import db, Song
from flask import request

class SongResource(Resource):
    def get(self):
        try:
            songs = Song.query.all()
            return {'songs': [song.serialize() for song in songs]}, 200
        except Exception as e:
            return {'message': 'Something went wrong', 'error': str(e)}, 500
    
    def post(self):
        try:
            song = Song(
                title=request.json['title'],
                artist=request.json['artist']
            )
            db.session.add(song)
            db.session.commit()
            return {'message': 'Song added successfully', 'song': song.serialize()}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': 'Something went wrong', 'error': str(e)}, 500
        
    def put(self):
        try:
            song = Song.query.get(request.json['id'])
            if not song:
                return {'message': 'Song not found'}, 404
            song.title = request.json['title']
            song.artist = request.json['artist']
            db.session.commit()
            return {'message': 'Song updated successfully', 'song': song.serialize()}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': 'Something went wrong', 'error': str(e)}, 500
    
    def delete(self):
        try:
            song = Song.query.get(request.json['id'])
            if not song:
                return {'message': 'Song not found'}, 404
            db.session.delete(song)
            db.session.commit()
            return {'message': 'Song deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': 'Something went wrong', 'error': str(e)}, 500

class CheckGuessResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            user_guess = data.get('song_name', '').strip().lower()
            song_id = data.get('song_id')

            if not user_guess or not song_id:
                return {'message': 'Guess and song ID are required'}, 400

            song = Song.query.get(song_id)
            if not song:
                return {'message': 'Song not found'}, 404

            correct_title = song.title.strip().lower()

            if user_guess == correct_title:
                return {'message': 'Correct guess! 🎉'}, 200
            else:
                return {
                    'message': 'Incorrect guess. Try again!',
                    'correct_song': song.title
                }, 200

        except Exception as e:
            return {'message': 'Error checking guess', 'error': str(e)}, 500
