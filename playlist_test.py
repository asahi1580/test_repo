import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

client_id = '52daefbfe55b4f14baf2ca49a6ee745a'
client_secret = '5329ddcdb1624154bf94c8c230390867'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = sys.argv[1]
playlist_data = sp.user_playlist('31ljsv2irs6y7cgnfg737awxg2fe',playlist_id)

id_list = []
for track in playlist_data['tracks']['items']:
    id = track['track']['id']
    id_list.append(id)

for music_id in id_list:
    s = sp.track(music_id)
    print(s['name'])