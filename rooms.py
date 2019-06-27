#location module for adventure.py
import json
import characters as char
import os




def get_loc(name): #read location from file
    """try to open saved room, if no saved open original."""
    try:
        file = open('visited/' + name +'.json')
        f = file.read()
        room = json.loads(f)
        file.close()
        return room
    except FileNotFoundError:
        file = open('rooms/' + name +'.json')
        f = file.read()
        room = json.loads(f)
        file.close()
        return room
    
def save_room(room):
    save = json.dumps(room)
    if not os.path.isdir('visited'):
        os.makedirs('visited')
    file = open('visited/' + str(room['name']) +'.json','w')
    file.write(save)
    file.close()



class Location():
    """Class to store location information for the player."""

    def __init__(self, room):
        """Set the Dictionary to class attributes."""
        self.name = room['name']
        self.description = room['description']
        self.items = room['items']
        self.north = room['north']
        self.east = room['east']
        self.south = room['south']
        self.west = room['west']
        self.npc = room['npc']

        self.init_NPC()
        
    def init_NPC(self):
        """Initialize NPCS"""
        for i in range(0, len(self.npc)):
            #A little confusing with all the npc
            self.npc[i] = char.NPC(char.get_npc(self.npc[i]))
            

    def npc2string(self):
        """Change npc back to string for json serialization."""
        for i in range(0, len(self.npc)):
            self.npc[i] = self.npc[i].name
            

    def describe(self):
        """describe the location with name and description"""
        print(self.name.upper() ,self.description, sep='\n')

    def move(self, d):
        """move player in a direction."""
        #copy npc back to string of name
        self.npc2string()
        
        save_room(self.__dict__) #write current modified room dict to file
                        #then rerun own init method to change room data 
        if d == 'n':
            self.__init__(get_loc(self.north))
        elif d == 'e':
            self.__init__(get_loc(self.east))
        elif d == 's':
            self.__init__(get_loc(self.south))
        elif d == 'w':
            self.__init__(get_loc(self.west))
            
        self.describe()

if __name__ == '__main__':
    #test
    current_room = Location(get_loc('room1'))
    print(current_room.name , current_room.description,
          current_room.south)
    print(current_room.npc)
    save_room(current_room.__dict__)
    
    
    


    
    
            



