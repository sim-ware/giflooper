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

# data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=" + YOUR_API_KEY + "&limit=5").read())
# print json.dumps(data, sort_keys=True, indent=4)

r = requests.get("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=" + YOUR_API_KEY + "&limit=5")
# r.status_code
# r.headers['content-type']
# r.encoding
print(r.text)
print(r.json())
