# Chose not to go with this package as it was fiddly and made more sense to  # #
# lessen dependencies and use the API itself.  # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# import giphypop
# g = giphypop.Giphy()
# print(g)
# results = [x for x in g.search('kitten')]
# print(results[0])

import json
import requests

YOUR_API_KEY = "02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh"
SEARCHTERMS = "doom"

r = requests.get("http://api.giphy.com/v1/gifs/search?q=" + SEARCHTERMS + "&api_key=" + YOUR_API_KEY + "&limit=5")

# print(r.text[0])
# print(r.json()[0])
r = r.json()
print(r['data'][0]['images']['original']['url'])

# TODO:
# Fetch 50 Results
# TODO:
# Return Random 25
# TODO:
# Loop through 25
