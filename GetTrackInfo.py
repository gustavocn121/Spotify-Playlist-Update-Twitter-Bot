from WritingPages import getAcessToken
from SpotifySecrets import *
import requests
import json


access_token = getAcessToken(clientID, clientSecret)
song_id = 0

def getTrackInfo(song_id):

    url = 'https://api.spotify.com/v1/tracks/'+ song_id
    getHeader = {
        "Authorization": "Bearer " + access_token

    }
    res = requests.get(url, headers=getHeader)
    res_json = res.json()
    return res_json

def limpa_info(TrackInfo):
    Song_Title = TrackInfo['name']
    ArtistsObj = TrackInfo['artists']
    Artists = [i['name'] for i in ArtistsObj]
    ArtistsStr = '' 
    for a in Artists:
        if Artists[(len(Artists)-1)] == a:
            ArtistsStr += a
        else:
            ArtistsStr +=   a + ', '
    return f'A música "{Song_Title}" por  {ArtistsStr} foi '


if __name__ == '__main__':
    id1 = '1FvU97lrWOG2NRxErh6OZz'
    trackinfo = getTrackInfo(id1)
    print(json.dumps(trackinfo, indent=2))
    limpa_info(trackinfo)