import requests

URL='https://api.pokemonbattle.me'
HEADERS={'Content-Type': 'application/json',
           'trainer_token': 'b6fb96a1fb451a35821eef8835b6e4b1'}
TOKEN='b6fb96a1fb451a35821eef8835b6e4b1'
body={ "name": "Добрый",
        "photo": "https://dolnikov.ru/pokemons/albums/079.png"}
body_name={ "pokemon_id": "14224",
            "name": "Бодрый",
            "photo": "https://dolnikov.ru/pokemons/albums/079.png"}
body_pokeball={ "pokemon_id": "14224" }

#Создание покемона
response_add_pokemon=requests.post(url=f'{URL}/pokemons',headers=HEADERS,json=body)
print(response_add_pokemon.text)

#Смена имени покемона
response_new_name=requests.put(url=f'{URL}/pokemons',headers=HEADERS,json=body_name)
print(response_new_name.text)

#Поймать покемона в покебол
response_add_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADERS,json=body_pokeball)
print(response_add_pokeball.text)