#main game command
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
    def __init__(self, p):
       cmd.Cmd.__init__(self) #initialize the command prompt
       

       self.prompt = p.name.title() + ': '

       p.location.describe() #describe location on boot

        #counts for messages
       self.empty_call = 0
       self.invalids = 0
    #define cmd functionality
    def emptyline(self):
        """Redefine cmd.Cmd to do nothing on empty line input."""
        if self.empty_call < 10:
            self.empty_call += 1
            pass
        else:
            self.empty_call = 0
            print("What would you like to do?")
    def default(self, line):
        """Redefine default message for non valid command."""
        print("Invalid Command")
        self.invalids += 1
        if self.invalids > 5:
            print("Enter \"help\" for list of commands.")
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
    def do_take(self, args):
        """Take an item and put it in inventory."""
        args = self.parse(args)
        for arg in args:
            #check for 'take all' if there are items in location
            if arg == 'all' and len(p.location.items) != 0:
                p.inventory += p.location.items
                for i in p.location.items:
                    print(i, 'added to inventory.')
                del p.location.items[:]
            #if 'take all' and there is nothing there
            elif arg == 'all' and len(p.location.items) == 0:
                print('Nothing to take here.')
                #taking a specific item if in location
            elif arg in p.location.items:
                pop = p.location.items.index(arg)
                item = p.location.items.pop(pop)
                p.inventory.append(item)
                print(item, 'added to inventory.')
            elif arg == '':
                print('What do you want to take?')
            else:
                print('There is no' , arg , 'to take.')
    def do_drop(self, args):
        """Drop an item out of inventory."""
        args = self.parse(args)
        for arg in args:
            if arg in p.inventory:
                pop = p.inventory.index(arg)
                i = p.inventory.pop(pop) #remove item from inventory
                p.location.items.append(i)#drop into your location
                print('-' + arg + ' dropped')
            else:
                print('You don\'t have a ' , arg)
    def do_use(self, args):
        """Use an item in your inventory."""
        args = self.parse(args)
        for arg in args:
            if arg in p.inventory:
                useable =items.use_it(arg) #use item accordingly
                if useable == True:
                    pass
                else: #if useable is false means it is destroyed
                    p.inventory.remove(arg)
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
        if len(p.location.items) == 0:
            print('nothing')
        for i in p.location.items:
             if len(p.location.items) > 1:   
                 if i != p.location.items[-1]:
                     print('a ' + i + ', ', end='')
                 else:
                     print('and a ' + i + '.')
             else:
                 print('a ' + i + '.')
        
    #directions
    def do_north(self, args):
        """Move character location north."""
        if p.location.north != None:
            p.location.move('n')
        else:
            print('You can not move north')
    def do_south(self, *args):
        """Move character location south."""
        if p.location.south != None:
            p.location.move('s')
        else:
            print('You can not move south')
    def do_east(self, *args):
        """Move character location east."""
        if p.location.east != None:
            p.location.move('e')
        else:
            print('You can not move east')
    def do_west(self, *args):
        """Move character location west."""
        if p.location.west != None:
            p.location.move('w')
        else:
            print('You can not move west')
            
        #misc game commands
    def do_bag(self, args):
        """List player current inventory."""
        if p.inventory:
            for item in p.inventory:
                print('-', item)
        else:
            print('inventory empty')

    def do_stats(self, args):
        """Show player stats"""
        print('health - ' ,'equiped - ' , 'attack - ' ,
              'coins - ' + str(p.coins) , sep='\n')
    def do_describe(self, *args):
        """describes your current location."""
        p.location.describe()

    def do_quit(self, *args):
        """Exit the Game."""
        done = 'n'
        while done == 'n':
            done = input('Would you like to save and exit? (y/n)')
            if done == 'y':
                p.location.npc2string()
                save_room(p.location.__dict__)
                save_player(p.__dict__, p.location.id)                
                print('Game has been saved!\nThanks for playing!')
                return True
            elif done == 'n':
                break
    #functions called be do_* methods
    def speak(self, arg):
        """Called by speak and talk"""
        for i in p.location.npc:
            if arg.lower() == i.name:
                i.talk()
            else:
                print(arg.title(), 'is not here.')
        
#if __name__ == "__main__":    
p = Player(load_player())
print("type 'help' for a list of commands '\n")
print(intro + '\n')
g = Game(p)    
g.cmdloop()
      
    
    
    
    

     
   
    
