from npc import NPC

class Enemy(NPC):
    """Enemy class for adventure game."""

    def __init__(self, info):
        super().__init__(info) #take same attributes as npc
        #enemy attributes
        self.alive = True
        self.health = 6
        self.attack = 2

    def attack_player(self):
        if self.alive == True: #if not dead
            print(self.name, 'attacked you')
            #pass attack power to amount damage player will take
            return self.attack 

    def death(self): #set alive to False so that it can't make moves
        if self.health <= 0:
            self.alive = False    


if __name__ == "__main__":
    test_info = {

        'location': 10,
        'name': 'skeleton',
        'description': 'A skeleton holding a long sword.',
        'speak': 'kfjgjsdkng'
        }
skeleton = Enemy(test_info)
print(skeleton.description)
skeleton.health = 0
skeleton.death()
print(skeleton.description)
