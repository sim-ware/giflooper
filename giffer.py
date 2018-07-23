import json
import requests
from random import shuffle

class Giffer:

    def __init__(self, searchterms):
        self.searchterms = searchterms
        self.response = ""
        self.gifs_list = []


    def makeRequest(self):
        self.response = requests.get(("http://api.giphy.com/v1/gifs/search?q="
                        + self.searchterms
                        + "&api_key=02KjSiPr9Ur2Hizm8HsEdgB0NXPJiNBh&limit=50"))


    def jsonifyResult(self):
        print(self.response)
        self.response = self.response.json()
        print(self.response)


    def getGifList(self, limit):
        for x in range(limit):
            print(self.response)
            a = self.response['data'][x]['images']['original']['url']
            self.gifs_list.append(a)

    def shuffleGifs(self):
        shuffle(self.gifs_list)
