import requests as requests


URL = 'https://akabab.github.io/superhero-api/api'

superheroes_ids = {}
superheroes = ['Hulk', 'Thanos', 'Captain America']
def get_ids():
    all_heroes = requests.get(URL + '/all.json' )
    # pprint(all_heroes.json())
    for hero in all_heroes.json():
        if hero['name'] in superheroes:

            superheroes_ids[hero['name']] = str(hero['id'])


superheroes_int = []
superheroes_stats = []
get_ids()


for id in superheroes_ids:
    response = requests.get(URL + '/powerstats/' + superheroes_ids[id] + '.json')
    superhero_stats = {id: response.json()}
    superheroes_stats.append(superhero_stats)



for superhero in superheroes_stats:
    for stat in superhero:
        intelligence = superhero[stat]['intelligence']
        superhero_int = {stat: intelligence}
        superheroes_int.append(superhero_int)


genius_int = 0
for hero in superheroes_int:
    for int_ in hero:
        if hero[int_] > genius_int:
            genius_int = hero[int_]
            genius = int_

print(f' Самый умный {genius}')

