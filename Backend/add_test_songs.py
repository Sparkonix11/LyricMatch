import requests
import json

# List of songs
songs = [
    {"title": "Shape of You", "artist": "Ed Sheeran"},
    {"title": "Blinding Lights", "artist": "The Weeknd"},
    {"title": "Levitating", "artist": "Dua Lipa"},
    {"title": "Rolling in the Deep", "artist": "Adele"},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars"},
    {"title": "Bad Guy", "artist": "Billie Eilish"},
    {"title": "Stay", "artist": "The Kid LAROI & Justin Bieber"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper"},
    {"title": "Someone Like You", "artist": "Adele"},
    {"title": "Thinking Out Loud", "artist": "Ed Sheeran"},
    {"title": "Perfect", "artist": "Ed Sheeran"},
    {"title": "Rockstar", "artist": "Post Malone ft. 21 Savage"},
    {"title": "Watermelon Sugar", "artist": "Harry Styles"},
    {"title": "Save Your Tears", "artist": "The Weeknd"},
    {"title": "Dance Monkey", "artist": "Tones and I"},
    {"title": "Good 4 U", "artist": "Olivia Rodrigo"},
    {"title": "All of Me", "artist": "John Legend"},
    {"title": "Happier", "artist": "Ed Sheeran"},
    {"title": "Bad Habits", "artist": "Ed Sheeran"},
    {"title": "Stressed Out", "artist": "Twenty One Pilots"},
    {"title": "Ride", "artist": "Twenty One Pilots"},
    {"title": "Heathens", "artist": "Twenty One Pilots"}
]

url = "http://127.0.0.1:5000/api/v1/song"

for song in songs:
    response = requests.post(url, json=song)
    
    if response.status_code == 201:
        print(f"Successfully added song: {song['title']} by {song['artist']}")
    else:
        print(f"Failed to add song: {song['title']} by {song['artist']}. Error: {response.status_code}")

