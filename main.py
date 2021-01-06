import requests
import json
from csv import writer
import pandas as pd
import os
from WritingPages import write_page
from shutil import copyfile, rmtree
from data_diff import data_diff
from GetTrackInfo import getTrackInfo, limpa_info
from tweet_update import post_tweet
import time
import sys
import colorama


while True:
        
    def prepara_data(Paginas):
        PagAtual = 0
        with open('full_tracklist.csv', 'w', encoding='cp1252', newline='') as full:
            oescritor = writer(full)
            oescritor.writerow(['id'])    
            while PagAtual <= Paginas:
                file = f'{os.getcwd()}\\Pages\\PlaylistPage_{PagAtual}.json'    
                with open(file, 'r', encoding ='cp1252') as o:
                    oftl = json.loads(o.read())
                    for t in oftl['items']:
                        oescritor.writerow([t['track']['id']])
                    

                PagAtual+=1


    lastPage = write_page()
    prepara_data(lastPage)


    if os.path.exists('last_tracklist.csv'):
        data_diff('full_tracklist.csv', 'last_tracklist.csv')
    else:
        copyfile('full_tracklist.csv', 'last_tracklist.csv')      
        rmtree('Pages')
        os.remove('full_tracklist.csv')
        os.system("main.py")
        time.sleep(3)
        sys.exit()


    tweet_txt = pd.read_csv('diff_data.csv', sep=',', )
    for row in tweet_txt.itertuples():
        tweet = ''
        if row[2] == 'added':
            diferenca = 'ADICIONADA à playlist'
        if row[2] == 'removed':
            diferenca = 'REMOVIDA da playlist'
        
        trackinfo_json = getTrackInfo(row[1])
        songURL = 'https://open.spotify.com/track/'+ row[1]
        time.sleep(60*1)
        tweet = limpa_info(trackinfo_json) + diferenca + f' {songURL}'

        post_tweet(tweet)
        time.sleep(3)


    copyfile('full_tracklist.csv', 'last_tracklist.csv')      
    rmtree('Pages')
    os.remove('full_tracklist.csv')
    os.remove('diff_data.csv')
    time.sleep(60*5)

