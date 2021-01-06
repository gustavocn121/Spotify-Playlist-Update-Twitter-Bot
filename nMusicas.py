import json
import os
def NMusicas(file):
    with open(file, 'r', encoding='cp1252') as arq:
        file_json = json.loads(arq.read())
        num = 0
        for t in  file_json['items']: 
            num += 1
        return num




if __name__ == '__main__':
    pass