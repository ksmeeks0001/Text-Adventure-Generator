#location module for adventure.py
import json
import npc
import os




def get_loc(id): #read location from file
    """try to open saved room, if no saved open original."""
    try:
        file = open('visited/room' + str(id) +'.json')
        f = file.read()
        room = json.loads(f)
        file.close()
        return room
    except FileNotFoundError:
        file = open('rooms/room' + str(id) +'.json')
        f = file.read()
        room = json.loads(f)
        file.close()
        return room
def save_room(room):
    save = json.dumps(room)
    if not os.path.isdir('adventure/visited'):
        os.makedirs('adventure/visited')
    file = open('visited/room' + str(room['id']) +'.json','w')
    file.write(save)
    file.close()



class Location():
    """Class to store location information for the player."""

    def __init__(self, room):
        """Set the Dictionary to class attributes."""
        self.id = room['id']
        self.name = room['name']
        self.description = room['description']
        self.items = room['items']
        self.north = room['north']
        self.east = room['east']
        self.south = room['south']
        self.west = room['west']
        self.npc = room['npc']

                 
            

    def describe(self):
        """describe the location with name and description"""
        print(self.name.upper() ,self.description, sep='\n')

    def move(self, d):
        """move player in a direction."""
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
    current_room = Location(get_loc(2))
    print(current_room.name , current_room.description,
          current_room.south)
    print(current_room.npc)
    save_room(current_room.__dict__)
    
    
    


    
    
            



