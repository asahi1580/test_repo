#第一引数に曲のID、第二にプレイリストのIDを指定
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

low_limit = 0.85
high_limit = 1.15

client_id = '52daefbfe55b4f14baf2ca49a6ee745a'
client_secret = '5329ddcdb1624154bf94c8c230390867'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

import_music_id = sys.argv[1]
import_playlist_id = sys.argv[2]
i = sp.track(import_music_id)
p = sp.playlist(import_playlist_id)
print("import music : "+i['name'])
print("import playlist : "+p['name'])


music_data = sp.audio_features(import_music_id)
music_data = music_data[0]

playlist_data = sp.user_playlist('31ljsv2irs6y7cgnfg737awxg2fe',import_playlist_id)

id_list = []
features = []
for track in playlist_data['tracks']['items']:
    id = track['track']['id']
    id_list.append(id)
features.extend(sp.audio_features(id_list))

match_idlist = []
for feature in features:
    if(feature['danceability']*low_limit < music_data['danceability'] < feature['danceability']*high_limit):
        if(feature['energy']*low_limit < music_data['energy'] < feature['energy']*high_limit):
            if(feature['tempo']*low_limit < music_data['tempo'] < feature['tempo']*high_limit):
                match_idlist.append(feature['id'])
                
for match in match_idlist:
    s = sp.track(match)
    print(s['name'])