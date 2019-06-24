import eel
import json
import template_generate
from forms import RoomForm

import sys
error = open('error.txt', 'w')
sys.stderr = error

@eel.expose
def create_room(data):
    with open(data['name'] + '.json', 'w') as room:
        for selected in data.keys():
            if data[selected] == 'None':
                data[selected] = None
        room.write(json.dumps(data))

def room_create_view():
    form = RoomForm()
    template_generate.refresh_template(r'room_form.html', form=form)
    eel.start('room_form.html')

if __name__ == "__main__":
    template_generate.setup_django()
    eel.init('static')
    room_create_view()
