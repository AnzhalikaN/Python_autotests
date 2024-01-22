import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': 'e09874eaf5cc0dfa0732f2b7744199cc'}

# body = {
#    "name": "generate",
#    "photo": "generate"
#}

# response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADERS, timeout=5)
# print(response.text)

# BODY = {
#    "pokemon_id": "28285",
#    "name": "Lapochka",
#    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
#}
# response = requests.put(url=f'{URL}/pokemons', json=BODY, headers=HEADERS, timeout=5)
# print(response.text)

pok = {
    "pokemon_id": "28285"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=pok, headers=HEADERS, timeout=5)
print(response.text)
