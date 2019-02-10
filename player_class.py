#player class
import json
import rooms
import os



def set_player_name():
        """gets and sets the players name."""
        done = 'n'
        while done == 'n':
            name = input("What is your name, Traveler? ")
            prompt = "You entered "+name+" is this correct? (y/n) "
            done = input(prompt)             
            if done == 'y':
                return name
def load_player():
    """load saved player if available"""
    
    done = False    
    while done == False:
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
            x = 0    
            for i in range(1,5):
                x += 1
                room = 'room' + str(x) +'.json'
                if os.path.isfile('visited/' + room):
                    os.remove('visited/' + room)
            done = True
            return player 
    

def save_player(player, id):
    player['location'] = id
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


if __name__ == "__main__":
    character = Player(load_player())
    print(character.location)
    print(character.__dict__)
    print(character.location.__dict__)
        
       
       
