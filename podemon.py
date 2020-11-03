import requests
from bs4 import BeautifulSoup

resp = requests.get('https://tw.portal-pokemon.com/play/pokedex/api/v1?pokemon_type_id[]=fire&pokemon_ability_id=&zukan_id_from=1&zukan_id_to=807')
dictData = resp.json()
# print(dictData["pokemons"])

for data in dictData["pokemons"]:
        print(data["pokemon_name"]," - ", data["pokemon_type_name"]," - ",data["pokemon_type_id"])
        
# soup = BeautifulSoup(resp.text, 'html5lib')
# print(soup)
# pokemon_type_id
# print(soup.h1.text)

# for posts in soup.find_all('div','pokemon-list--box__type size-12 pokemon-list--box__type--fire'):
#     for post in posts.stripped_strings:
#         print(post)

# <div class="pokemon-list--box__types"><div class="pokemon-list--box__type size-12 pokemon-list--box__type--fire"><span>火</span></div></div>


# for title in soup.find_all('div','pokemon-list--box--wrapper'):
#     print(title.a)

# print(soup.find_all('div','pokemon-list--box--wrapper'))
# for posts in soup.find_all('div','pokemon-list--box__types'):
#     print(posts)
        
