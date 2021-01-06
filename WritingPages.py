import requests, base64, json
from SpotifySecrets import *
from nMusicas import NMusicas
import os
import os.path
from os import path

authUrl = "https://accounts.spotify.com/api/token"
authHeader = {}
authData = {}

# Acess Token
def getAcessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = 'client_credentials'

    res = requests.post(authUrl, headers=authHeader, data=authData)

    responseObject = res.json()


    acessToken = responseObject['access_token']
    return acessToken
# Playlist page
def getPlaylsitTracks(token, playlistID, playlistEndPoint):
    # GET https://api.spotify.com/v1/playlists/{playlist_id}/tracks
    getHeader = {
        "Authorization": "Bearer " + token

    }
    res = requests.get(playlistEndPoint, headers=getHeader)
    playlistObject = res.json()
    return playlistObject


def write_page(): 
    # API requests
    token = getAcessToken(clientID, clientSecret)
    playlistID = YourPlaylist_ID
    offset = 0
    playlistEndPoint = f'https://api.spotify.com/v1/playlists/{playlistID}/tracks?limit=100&fields=items(track(id))&offset='+ str(offset)
    trackjson = getPlaylsitTracks(token, playlistID, playlistEndPoint)

    if not os.path.exists("Pages"):
        os.mkdir('Pages')


    page = 0
    file = f'{os.getcwd()}\\Pages\\PlaylistPage_{str(page)}.json'
    with open(file, 'w', encoding='cp1252') as f:
        json.dump(trackjson, f)
    path = os.getcwd()


    while NMusicas(file)==100:
        offset += 100
        page +=1
        playlistEndPoint = f'https://api.spotify.com/v1/playlists/{playlistID}/tracks?limit=100&fields=items(track(id))&offset='+ str(offset)
        trackjson = getPlaylsitTracks(token, playlistID, playlistEndPoint)
        file = f'{path}\\Pages\\PlaylistPage_{str(page)}.json'
        with open(file, 'w', encoding='cp1252') as f:
            json.dump(trackjson, f)

    lastPage = page
    return lastPage

