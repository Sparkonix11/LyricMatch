from flask import request
from flask_restful import Resource
from models import Song
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import random

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

class RandomLyric(Resource):
    def get(self):
        try:
            songs = Song.query.all()
            if not songs:
                return {'message': 'No songs found in the database'}, 404

            selected_song = random.choice(songs)

            # prompt = f"Generate a short 2-4 lines lyric snippet from the song '{selected_song.title}' by {selected_song.artist}."
            
            # response = client.models.generate_content(
            #     model="gpt-4o-mini",
            #     messages=[{"role": "system", "content": "You are a songwriter."},
            #               {"role": "user", "content": prompt}]
            # )

            response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            config=types.GenerateContentConfig(
                                system_instruction="You are a songwriter."),
                            contents= f"Generate a short 2-4 lines lyric snippet from the song '{selected_song.title}' by {selected_song.artist}. and just respond with lyrics"
                        )

            lyric_snippet = response.text
            
            return {
                'lyric_snippet': lyric_snippet,
                'song_id': selected_song.id
            }, 200

        except Exception as e:
            return {'message': 'Error generating lyric snippet', 'error': str(e)}, 500