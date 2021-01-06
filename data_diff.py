import csv
import pandas as pd
import time
from os import system
from GetTrackInfo import getTrackInfo, limpa_info
import colorama
from datetime import datetime

colorama.init(autoreset=True)


def data_diff(NewData, LastData):

    data = pd.read_csv(NewData, encoding='cp1252')
    old_data = pd.read_csv(LastData, encoding='cp1252')

    add = []
    removidas = []
    qtd_musicas1 = len(data.index)
    qtd_musicas2 = len(old_data.index)
    total_execucoes = qtd_musicas1 + qtd_musicas2 
    execucoes_concluidas = 0
    inicio1 = time.time()


    #-------------------             ADD                   -----------------------------------------------
    for indexa,rowa in data.iterrows():
        system('cls')    
        print("\033[36m" + '|     Comparando Dados...     |')
        print('\033[36m'+'-------------------------------')        
        print(f'{round((execucoes_concluidas/total_execucoes), 2)*100}% concluido  - {indexa} - {rowa["id"]}')        
        for indexb,rowb in old_data.iterrows():

            if (rowa['id'] == rowb['id']):
                igual = True
                break
            else:
                igual = False
        if not igual:
            add.append(rowa['id'])
        execucoes_concluidas += 1
    fim1 = time.time()
    dif1 = fim1 - inicio1
    
    
    #-------------------             REMOVIDOS                   --------------------------------------------
    inicio2 = time.time()
    for indexa,rowa in old_data.iterrows():
        system('cls')
        print('\033[36m'+'|     Comparando Dados...     |')
        print('-------------------------------')
        print(f'{round((execucoes_concluidas/total_execucoes), 2)*100}% concluido  - {indexa} - {rowa["id"]}')
        for indexb,rowb in data.iterrows():
            
            if (rowa['id'] == rowb['id']):
                igual = True
                break
            else:
                igual = False
        if not igual:
            removidas.append(rowa['id'])
        execucoes_concluidas += 1
    system('cls')
    print('|     \033[32mAnalise concluida     \033[39m|')
    print('-----------------------------\n\n')
    fim2 = time.time()
    dif2 = fim2 - inicio2 


    #-------------------             PRINT DIFF                   --------------------------------------------
    for t in add:
        print(f'a musicas de id ={t} foi \033[32mADICIONADA \033[39mà playlist')
    #    print(f'https://open.spotify.com/track/{t}?si=bDqZwsabTy2QAS6fPoxUXQ')
    for t in removidas:
        print(f'a musicas de id ={t} foi \033[31mREMOVIDA \033[39mda playlist')
    totaltempo = dif1+dif2

    #-------------------             tweets txt                   --------------------------------------------
    
    with open('diff_data.csv', 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(['id','diff'])
        for sid in add:
            escritor.writerow([sid,'added'])
        for sid in removidas:
            escritor.writerow([sid,'removed'])
        

        
    
    #-------------------             TEMPO DE EXECUCAO                   --------------------------------------
    print(f'tempo de execucao  1 = {round(dif1, 2)} segundos')
    print(f'tempo de execucao  2 = {round(dif2, 2)} segundos')
    print(f'tempo de execucao  total = {round(totaltempo, 2)} segundos')
    print(f'fim da execucao em: {datetime.now()}')


if __name__ == "__main__":
    data_diff('full_tracklist.csv', 'last_tracklist.csv')


    
    