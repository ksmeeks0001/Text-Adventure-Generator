#npc module for adventure
import json

def get_npc(name): #read npc info from file 
    file = open('characters/'+name +'.json')
    f = file.read()
    npc = json.loads(f)
    return npc

class NPC():
    def __init__(self, info): #info = dictionary read in from json
        self.location = info['location']
        self.name = info['name']
        self.description = info['description']
        self.speak = info['speak']

    def describe(self):
        """print description"""
        print(self.description)

    def talk(self):
        """print what npc says to player"""
        print(self.speak)

if __name__ == "__main__":
    keeper = NPC(get_npc("inn keeper"))
    keeper.talk()
    
        
