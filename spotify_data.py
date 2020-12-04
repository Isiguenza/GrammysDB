
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 


client_id = '...'
client_secret = '...'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('1295436360', '5Mpn3yWXwUMck2WpTcTe18')

print(len(ids))
print(ids)

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)


  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  


  track = [album, artist, length,release_date]
  return track

  

tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ['nombre', 'album', 'artista', 'duracion', 'anio'])
df.to_csv("spotify.csv", sep = ',')