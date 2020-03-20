from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

# connects to the API using the official RamblerFy api credentials I set up

client_credentials_manager = SpotifyClientCredentials(client_id="318bd146dc0b46bd9e41e990bbe4ce2a",
                                                      client_secret="c56fe1ad00454247b966648148405c19", proxies=None,
                                                      requests_timeout=None)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Turn this to TRUE to see all the HTTP exchanges between us and the API
# Turn this to False for pretty output
sp.trace = False

start = time.time()
# For seeing how long each call takes

# Get the audio features for a sample/test track
''' TODO Change this so we can get data for an artist, song title, or playlist ' \
We can use the search function of the API:
(https://developer.spotify.com/documentation/web-api/reference/search/search/)'''
audio_features = sp.audio_features("spotify:track:2r1iA9msqYx0mA4m3KdFmS")
# audio_analysis = sp.audio_analysis("11dFghVXANMlKmJXsNCbNl")

duration_ms = audio_features[0]["duration_ms"]
loudness = audio_features[0]["loudness"]
tempo = audio_features[0]["tempo"]
key = audio_features[0]["key"]
danceability = audio_features[0]["danceability"]
energy = audio_features[0]["energy"]
valence = audio_features[0]["valence"]
track_id = audio_features[0]["uri"]
track_info = sp.track(track_id)
track_name = track_info["name"]
track_artist = track_info["artists"][0]["name"]
tract_audio_features_dict = {
    "track_name": track_name,
    "track_artist": track_name,
    "duration_ms": duration_ms,
    "loudness": loudness,
    "tempo": tempo,
    "key": key,
    "danceability": danceability,
    "energy": energy,
    "valence:": valence
}
delta = time.time() - start
print("Track is " + track_name)
print("Artist is " + track_artist)
print("---------------------\nAudio Features we want \n---------------------")
print(json.dumps(tract_audio_features_dict, indent=4))

print("Data retrieved in %.2f seconds" % (delta,))
with open(track_name + '.json', 'w') as file_out:
    json.dump(tract_audio_features_dict, file_out, indent=4, sort_keys=True)
