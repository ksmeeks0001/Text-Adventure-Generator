import json

def main():
    print("Room Create (capitilization only required on description and items)")
    room = {}
    room['name'] = input('NAME: ').title()
    room["description"] = input('\nDescription:\n\t')
    print("ENTER NAME OF CONNECTING LOCATIONS OR BLANK FOR NONE")
    room["north"] = input('Room North: ').title()
    room["south"] = input('Room South: ').title()
    room["east"] = input('Room East: ').title()
    room["west"] = input('Room West: ').title()
    room['npc'] = []
    room['items'] = []

    conv_direct(room,'north')
    conv_direct(room,'south')
    conv_direct(room,'east')
    conv_direct(room,'west')

    npcs = ''
    while not npcs.isdigit():
        try:
            npcs = input('how many npcs? ')
        except:
            continue
    for i in range(int(npcs)):
        room['npc'].append(input('Name of npc: '))

    items = ''
    while not items.isdigit():
        try:
            items = input('How many items? ')
        except:
            continue
    for i in range(int(items)):
        room['items'].append(input('name of item: '))

    for key, value in room.items():
        print(key, value)

    file = '..\\rooms\\' + room['name'] + '.json'
    with open(file, 'w') as f:
        save = json.dumps(room)
        f.write(save)

def conv_direct(room, direction):
    if room[direction] == '':
         room[direction] = None

main()
input()
