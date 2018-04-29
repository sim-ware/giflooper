import json
import requests
import random

YOUR_API_KEY = "02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh"
SEARCHTERMS = "zelda"
LIMIT=100

r = requests.get("http://api.giphy.com/v1/gifs/search?q=" + SEARCHTERMS + "&api_key=" + YOUR_API_KEY + "&limit=" + str(LIMIT))

r = r.json()
# print(r['data'][0]['images']['original']['url'])

gifs_list = []
for x in range(LIMIT):
    a = r['data'][x]['images']['original']['url']
    gifs_list.append(a)
# print(gifs_list)

my_randoms = random.sample(range(100), 25)
# print(my_randoms)

resultloop = [gifs_list[i] for i in my_randoms]
print(resultloop)
# TODO: Return Random 25
# TODO: Have 25 random no.s between 1-50 in array
# TODO: use them as keys to pop the data into another array

# L = ['ant', 'bread', 'cat', 'donkey', 'elephant', 'frank', 'giraffe', 'horsey']
# Idx = [0, 3, 7]
# T = [L[i] for i in Idx]
# print(T)
