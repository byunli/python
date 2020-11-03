import requests
from bs4 import BeautifulSoup

resp = requests.get('https://tw.portal-pokemon.com/play/pokedex')
soup = BeautifulSoup(resp.text, 'html5lib')

for a in soup.find_all('a'):
    for post in a.stripped_strings:
        print(post)


# for title in soup.find_all('a'):
#     print(title)

# for posts in soup.find_all('div',{'class':'pokemon-list--box__name','class':'size-22'}):
    # for post in posts.stripped_strings:
    #     print(post)
    