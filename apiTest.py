import requests
import json
import random

def jsonPrint(t):
    
    data = json.loads(json.dumps(t))
    shows = [i['title'] for i in data]
    recs = []
    while len(recs) < 10:
        c = random.choice(shows)
        if c in recs:
            continue
        recs.append(c)
        print(recs)

response = requests.get('https://imdb-api.com/en/API/MostPopularTVs/k_1a0ypmno')

jsonPrint(response.json()['items'])