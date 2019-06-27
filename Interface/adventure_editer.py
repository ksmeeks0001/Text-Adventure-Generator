#generates views from django and displays with eel
import os
import eel
import template_generate
from forms import RoomForm
import json
#from exposed_functions import create_room, fill_room_form

import sys
error = open('error.txt', 'w')
sys.stderr = error


@eel.expose
def room_create_view(room=False):
    if room:
        context = {'edit': True}
        for key in room.keys():
            if room[key] == None:
                room[key] = 'None'
        if len(room['npc']) == 0:
            room['npc'].append('None')
        if len(room['items']) == 0:
            room['items'].append('None')
        context['items'] = room['items']
        context['npc'] = room['npc']
        form = RoomForm(room)
    else:
        form = RoomForm()
        context = {'edit': False}
        context['items'] = []
        context['npc'] = []

    template_generate.refresh_template(r'room_form.html', form=form, context=context)



@eel.expose
def room_list_view():
    rooms = list()
    for file in os.listdir('../rooms'):
        file = file.split('.')[0] #remove file extension
        rooms.append(file)
    context = {'rooms': rooms}
    template_generate.refresh_template('display_rooms.html', context=context)
    

@eel.expose
def create_room(data):
    data['name'] = data['name'].title()
    with open("../rooms/"+data['name'] + '.json', 'w') as room:
        for selected in data.keys():
            if data[selected] == 'None':
                data[selected] = None
            elif data[selected] == ['None']:
                data[selected] = []
        room.write(json.dumps(data))

@eel.expose
def fill_room_form(room):
    """get room data and call room_create_view with dict"""
    with open('../rooms/'+room +'.json') as file:
        data = json.loads(file.read())
    print('right after loading', data)
    room_create_view(room=data)
    
if __name__ == "__main__":
    template_generate.setup_django()
    eel.init('static')
    room_list_view()
    #room_create_view()
    eel.start('display_rooms.html')
    #eel.start('room_form.html')

