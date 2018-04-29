import json
import requests
import random



# Constants & Keys
YOUR_API_KEY = "02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh"
SEARCHTERMS = "zelda"
LIMIT=100


# HTTP Request
r = requests.get(("http://api.giphy.com/v1/gifs/search?q="
                + SEARCHTERMS
                + "&api_key="
                + YOUR_API_KEY
                + "&limit="
                + str(LIMIT)))


# Turn Request to JSON
r = r.json()


# Create a List of the URLs of the returned GIF search-data
gifs_list = []
for x in range(LIMIT):
    a = r['data'][x]['images']['original']['url']
    gifs_list.append(a)


# Fetch 25 random numbers in the range of the LIMIT
randomers = random.sample(range(LIMIT), 25)


# Use the randomers to filter the GIFURL List to get our ResultLoop URLs.
resultloop = [gifs_list[i] for i in randomers]
print(resultloop)
