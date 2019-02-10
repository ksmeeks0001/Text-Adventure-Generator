TEXT ADVENTURE GAME

player_class.py: 
	
	load_player(): Check if game should be continued from a save.

	set_player_name(): Getting input for player name. 
	
	save_player(player, id): 

	CLASS Player(info):
		Info is a dictionary read from json file. 
		
		Attributes: 
			name
			location
			inventory
			coins
			
rooms.py:
	
	get_loc(id):
		Attempts to load json of a visited version of a location.
		Loads default on fail.

	save_room(room): Saves Location to json file in visited directory

	CLASS Location(room):
		Room is dictionary read in from the json file.
	
		Attributes:
			id, name, description, items, north, east, south,
			west, npc.

		describe(): prints locations name and description

		move(d):
			d is direction of move
			Saves self to json.
			Reinitialize self with next locations info.

json_room_create:
	script to create rooms in json format.

npc.py:
	
	get_nps(name): open npc json file return dictionary

	CLASS NPC(info):
		Info is disctionary read from json file.
		
		Attributes:
			location, name, description, speak
	
		describe(): print description
	
		talk(): print speak

adventure.py:
	
	CLASS Game(p):
		Derives from cmd.Cmd
		p is an instance of Player.
	
		Defines all user commands. (See Defined commands)



			

		
		
	
