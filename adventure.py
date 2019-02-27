#main game command
from os import system
import cmd
from rooms import*
from characters import*
from player_class import*
import json
import items
intro = 'You just arrived to a small village. '
intro += 'It is beggining to get dark. You have been '
intro += 'on a long journey from your homeland in '
intro +='search of glory and honor.'

class Game(cmd.Cmd):
    def __init__(self, player):

       cmd.Cmd.__init__(self) #initialize the command prompt    
       self.player = player 
       self.prompt = self.player.name.title() + ': '
       self.doc_header = "Player Commands      Type 'help <command>' for details'"
       self.ruler = '*'
       
       #counts for messages
       self.empty_call = 0
       self.invalids = 0
       #move counter
       self.moves = 0

    #define cmd functionality
    def preloop(self):
        print('\n' * 100)
        self.player.location.describe() #describe location on boot

    def precmd(self, line):
        print('\n' * 5)
        self.moves += 1
        return line.lower()

    def emptyline(self):
        """Redefine cmd.Cmd to do nothing on empty line input."""
        if self.empty_call <= 5:
            self.empty_call += 1
        elif self.empty_call < 10 :
            print("What would you like to do?")
            self.empty_call += 1
        else:
            self.empty_call = 0
            self.do_help('')

    def default(self, line):
        """Redefine default message for non valid command."""
        self.invalids += 1
        if self.invalids <= 5:
            print("What do you mean by '"+line+"'")
        elif self.invalids < 7:
            print("Enter \"help\" for list of commands.")
        else:
            reply = input("Do you need some help? ")
            if (reply.lower() == 'y') or (reply.lower() == 'yes'):
                self.do_help('');
            self.invalids = 0

    #argument parser
    def parse(self, args):
        if ',' in args:
            args = args.split(',')
            for i in range(0,len(args)):
                args[i] = args[i].strip()
            return args
        else:
            args = args.split()
            for i in range(0,len(args)):
                args[i] = args[i].strip()
            return args

    #actions
    def do_take(self, arg):
        """Take an item and put it in inventory."""
    
        #check for 'take all' if there are items in location
        if arg == 'all' and len(self.player.location.items) != 0:
            self.player.inventory += self.player.location.items
            for i in self.player.location.items:
                print(i, 'added to inventory.')
            del self.player.location.items[:]
        #if 'take all' and there is nothing there
        elif arg == 'all' and len(self.player.location.items) == 0:
            print('Nothing to take here.')
        #taking a specific item if in location
        elif arg in self.player.location.items:
            pop = self.player.location.items.index(arg)
            item = self.player.location.items.pop(pop)
            self.player.new_item_data(item)
            print(item, 'added to inventory.')
        elif arg == '':
            print('What do you want to take?')
        else:
            print('There is no' , arg , 'to take.')

    def do_drop(self, arg):
        """Drop an item out of inventory."""
        if arg in self.player.inventory.keys():
            self.player.location.items.append(arg)#drop into your location
            del self.player.inventory[arg]
            print('-' + arg + ' dropped')
        else:
            print('You don\'t have a ' , arg)

    def do_use(self, arg):
        """Use an item in your inventory."""
        if arg == '':
            print("What do you want to use?")
        elif arg in self.player.inventory.keys():
            self.player.inventory[arg].use(self.player)
            if not self.player.inventory[arg].reusable:
                del self.player.inventory[arg]
        else:
            print('You don\'t have a ' , arg)

    def do_speak(self, arg):
        """speak to a character"""
        self.speak(arg)

    def do_talk(self, arg):
        """speak to a character"""
        self.speak(arg)

    def do_search(self, args):
        """search your location for items."""
        print('After searching you found' , end=' ')
        if len(self.player.location.items) == 0:
            print('nothing')
        for i in self.player.location.items:
             if len(self.player.location.items) > 1:   
                 if i != self.player.location.items[-1]:
                     print('a ' + i + ', ', end='')
                 else:
                     print('and a ' + i + '.')
             else:
                 print('a ' + i + '.')
        
    #directions
    def do_north(self, args):
        """Move character location north."""
        if self.player.location.north != None:
            self.player.location.move('n')
        else:
            print('You can not move north')

    def do_south(self, *args):
        """Move character location south."""
        if self.player.location.south != None:
            self.player.location.move('s')
        else:
            print('You can not move south')

    def do_east(self, *args):
        """Move character location east."""
        if self.player.location.east != None:
            self.player.location.move('e')
        else:
            print('You can not move east')

    def do_west(self, *args):
        """Move character location west."""
        if self.player.location.west != None:
            self.player.location.move('w')
        else:
            print('You can not move west')
            
        #misc game commands
    def do_bag(self, args):
        """List player current inventory."""
        if self.player.inventory:
            for item in self.player.inventory:
                print('-', item)
        else:
            print('inventory empty')

    def do_stats(self, args):
        """Show player stats"""
        print('health - ' ,'equiped - ' , 'attack - ' ,
              'coins - ' + str(self.player.coins) , sep='\n')

    def do_describe(self, arg):
        """Describes a person, place or thing."""
        #no arg describe location
        if not arg:
            self.player.location.describe()
        elif arg.lower() == "here" or arg.lower() == "location":
            self.player.location.describe()
        else:
            for npc in self.player.location.npc:
                if arg == npc.name.lower():
                    npc.describe()
                    return
            for item in self.player.inventory.keys():
                if arg == item:
                    self.player.inventory[item].describe()
                    return           
            
            print("What is a "+arg+"?")

    def do_quit(self, *args):
        """Exit the Game."""
        done = 'n'
        while done == 'n':
            done = input('Would you like to save and exit? (y/n)')
            if done == 'y':
                self.player.location.npc2string()
                save_room(self.player.location.__dict__)
                save_player(self.player.__dict__,
                            self.player.location.id,
                            list(self.player.inventory.keys()))                
                print('Game has been saved!\nThanks for playing!')
                return True
            elif done == 'n':
                break

    #functions called by do_* methods
    def speak(self, arg):
        """Called by speak and talk"""
        if arg == "":
            print("Who do you want to speak to?")
        else:
            for i in self.player.location.npc:
                if arg.lower() == i.name:
                    i.talk()
                else:
                    print(arg.title(), 'is not here.')
        
#if __name__ == "__main__":
print("Welcome to Kevin's Text Adventure!!")
p = Player(load_player())
print("type 'help' for a list of commands '\n")
print(intro + '\n')
g = Game(p)   
g.cmdloop()
      
    
    
    
    

     
   
    
