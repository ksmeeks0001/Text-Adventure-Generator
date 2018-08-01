# Text-Adventure-Generator
Users can create their own text adventure maps, characters, stories and items.


The goal of this project is to ceate a system that anyone can use to make a text adventure game.
Player input is done using cmd module.
players, locations, npc all read from json files.
***************************************************************************************
player_class.py - defines player class and functions that load/save player to file
		holds an instance of Location class
		  
rooms.py - defines functions for reading/writing location info.
	   visited rooms are saved to seperate folder and are tried to be opened first.
	
	   defines Location class, takes dictionary read in from json file.

npc.py - function for reading npc information from .json
	 defines NPC class

enemy.py - defines enemy class for battles (not yet implemented into main game)

gui.py - goal is to show player stats during game for quick reference

adventure.py - creates 'Game' class inheriting from cmd.Cmd
		loads player
		commands are read in from players keyboards via cmd
items.py - function for deciding what to do when an item is used
json_room_create.py - tool to create a new location 
			input information when prompted
			saved to json file
*******************************************************************************************
There is a lot of work to be done in order toachieve the goal.

1. Need a tool that creates npc and enemy json files the same way json_room_create.py works
2. all npcs should be moved to npc folder
3. item class should be created with description and use_it methods.
	items should be created and utilized as json files as well for easy creating.
4. write tests to ensure everything works as planned and to be used as features are added 
	to make sure nothing breaks.
5. fighting should be implemented
	attack points, HP, defense points
	how do enemies attack you or get attacked ect.
6. armor/wielding weapons
7. merchants/ in game currency            
