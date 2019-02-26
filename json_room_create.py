import json

def main():

    room_num = int(input("Enter the room number you want to add. "))
    room = {}
    room['id'] = room_num
    room['name'] = input('NAME: ')
    room["description"] = input('\nDescription:\n\t')
    print("(ENTER ID NUMBER FOR DIRECTIONS)")
    room["north"] = input('Room North: ')
    room["south"] = input('Room South: ')
    room["east"] = input('Room East: ')
    room["west"] = input('Room West: ')
    room['npc'] = []
    room['items'] = []

    conv_direct(room,'north')
    conv_direct(room,'south')
    conv_direct(room,'east')
    conv_direct(room,'west')


    npcs = int(input('how many npcs? '))
    for i in range(npcs):
        room['npc'].append(input('Name of npc: '))

    items = int(input('How many items? '))
    for i in range(items):
        room['items'].append(input('name of item: '))

    for key, value in room.items():
        print(key, value)

    file = 'rooms/room' + str(room_num) + '.json'
    with open(file, 'w') as f:
        save = json.dumps(room)
        f.write(save)

def conv_direct(room,direction):
    if room[direction] != None:
         room[direction] = int(room[direction])
main()
input()
