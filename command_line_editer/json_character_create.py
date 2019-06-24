import json

def main():

    character = dict()
    character['name'] = input("Name of the character: ")
    character['location'] = input("Enter location ID: ")
    character['description'] = input("Character Description: ")
    character['speak'] = input("What will the character say? ")

    for i in character.keys():
        if (i != 'speak') and character[i] == '':
            print("Must enter a valid "+i)
            return 

    try:
        character['location'] = int(character['location'])
    except:
        print("Must enter a valid integer for location ID")
        return 
    file = 'characters/'+character['name']+'.json'
    with open(file,'w') as f:
        save = json.dumps(character)
        f.write(save)


main()
input()
    
