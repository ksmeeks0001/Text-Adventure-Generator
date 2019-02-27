#player class
import json
import rooms
import os
from items import*
import pickle
from shutil import rmtree

def set_player_name():
        """gets and sets the players name."""
        redo = 0
        while True:
            redo += 1
            if redo > 6:
                print("Are you having trouble?")
                redo = 0
            name = input("What is your name, Traveler? ")
            if name:
                prompt = "You entered "+name+" is this correct? (y/n) "
                correct = input(prompt)
                if correct.lower() == 'y':
                        return name
                else:
                        continue
                
                
def load_player():
    """load saved player if available"""
    
    done = False    
    while not done:
        load = input('Continue saved game? (y/n) ')
        if load == 'y':           
            try:
                file = open('players/player.json')
                f = file.read()
                player = json.loads(f)
                file.close()
                return player
                
            except:
                print('No saved game found.')
                continue   
            
        else: #start a new character
            file = open('players/new.json')
            f = file.read()
            player = json.loads(f)
            file.close()
            player['name'] = set_player_name()
            try:
                rmtree('visited')
               
            except:
                    pass
            done = True
            return player 
    

def save_player(player, id, itemkeys):
    player['location'] = id
    player['inventory'] = itemkeys
    save = json.dumps(player)
    file = open('players/player.json','w')
    file.write(save)
    file.close()




class Player():
    """The player of the game."""

    def __init__(self, info):
        #player attributes        
       self.name = info['name'] #name of the player        
       self.location = rooms.Location(rooms.get_loc(info['location']))    
       self.inventory = info['inventory']
       self.coins = info['coins']
       self.init_item_data()

    def init_item_data(self):
        """Get Item data from pickle file."""
        items = dict()
        for i in self.inventory:
            with open('items/'+i+'.pickle', 'rb') as file:
                items[i] = pickle.load(file)
        self.inventory = items
        
    def new_item_data(self, item):
        """Get Item data after picking it up."""
        with open('items/'+item+'.pickle','rb') as file:
            self.inventory[item] = pickle.load(file)


#tests
if __name__ == "__main__":
    character = Player(load_player())
    print(character.location)
    print(character.__dict__)
    print(character.location.__dict__)
        
       
       
