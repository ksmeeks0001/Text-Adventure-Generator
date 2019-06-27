#all django forms for interface

from django import forms
import os



import sys
error = open('error.txt', 'w')
sys.stderr = error

class RoomForm(forms.Form):
    name = forms.CharField(label="Name")
    description = forms.CharField(label="Description", widget = forms.Textarea)
    empty = ('None','None')
    
    ITEM_CHOICES = [empty]
    for item in os.listdir(r'C:\Users\kevsm_000\Documents\adventure\remote\items'):
        item = item.split('.') #remove file extension
        ITEM_CHOICES.append( ('item', item[0]) )
        
    items = forms.MultipleChoiceField(label="Items", choices=ITEM_CHOICES)

    NPC_CHOICES = [empty]
    for npc in os.listdir(r'C:\Users\kevsm_000\Documents\adventure\remote\characters'):
        npc = npc.split('.')
        NPC_CHOICES.append( ('character', npc[0]) )
        
    npcs = forms.MultipleChoiceField(label="NPCs", choices=NPC_CHOICES)

    DIRECTION_CHOICES = [empty]
    for room in os.listdir(r'C:\Users\kevsm_000\Documents\adventure\remote\rooms'):
        room = room.split('.')
        DIRECTION_CHOICES.append( ('room', room[0]) )
    
    north = forms.ChoiceField(label="North", choices= DIRECTION_CHOICES)
    south = forms.ChoiceField(label="South", choices= DIRECTION_CHOICES)
    west = forms.ChoiceField(label="West", choices= DIRECTION_CHOICES)
    east = forms.ChoiceField(label="East", choices= DIRECTION_CHOICES)
    


 
        
    
