import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

#Authentication from spotify for developers
auth_manager = SpotifyClientCredentials('fdc54e50a3d045189b2e053211573026','7dafcb2c1a8147d5be08cb931f65ee5f')
sp = spotipy.Spotify(auth_manager=auth_manager)

def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids

def getTrackFeatures(id):
    track_info = sp.track(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    # release_date = track_info['album']['release_date']
    # length = track_info['duration_ms']
    # popularity = track_info['popularity']

    track_data = [name, album, artist] #, release_date, length, popularity
    return track_data

# Code for creating dataframe of feteched playlist
#The playlist to be fetched
emotion_dict = {0:"Angry",1:"Disgusted",2:"Fearful",3:"Happy",4:"Neutral",5:"Sad",6:"Surprised"}
music_dist={0:"https://open.spotify.com/playlist/7w2gdtZB1TpQcuKpjNGYAr?si=0a0d21f9722e4f86",1:"https://open.spotify.com/playlist/4QX9puYF2VuG5Q8IrSV2A7?si=ce47957c0b1e4628",2:"https://open.spotify.com/playlist/5AM4lgcUAw5sokybXj3ny7?si=76e6cac5043648b0",3:"https://open.spotify.com/playlist/1ZKdvf5yXvwVyzgznVz2Nl?si=75a0ea1d693649dd",4:"https://open.spotify.com/playlist/7EClwmhqu7mg4JvUI9z5DT?si=decba5dc1f114f49",5:"https://open.spotify.com/playlist/1gd8rPLzo3bjk1yyQce0h7?si=cae63ecb3e554f79",6:"https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik?si=0b473734554749d9"}

#Saving all the tracks in excel file

# track_ids = getTrackIDs('spotify',music_dist[0])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/angry.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[1])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/disgusted.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[2])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/fearful.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[3])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/happy.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[4])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/neutral.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[5])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/sad.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify',music_dist[6])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns = ['Name','Album','Artist']) # ,'Release_date','Length','Popularity'
#     df.to_csv('songs/surprised.csv')
# print("CSV Generated")