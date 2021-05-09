import requests
from pprint import pprint
class Super_Hero:
    url = ' https://superheroapi.com/api/'
    access_token = '2619421814940190'
    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intelligence = ''
    def get_id(self):
        self.id = requests.get(self.url + self.access_token + '/search/' + self.name).json()['results'][0]['id']
        return self.id
    def get_intelligence(self):
        if not self.id:
            self.get_id()
        self.intelligence = requests.get(self.url + self.access_token + '/' + self.id + '/powerstats').json()['intelligence']
        return self.intelligence
    
if __name__ == "__main__":
    Super_Heros = [Super_Hero('Hulk'),
                   Super_Hero('Captain America'),
                   Super_Hero('Thanos')]
    print(Super_Heros[0].get_intelligence())
