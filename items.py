

class Item():
    """Item Base Representation."""

    def __init__(self,name,description, reusable):
        self.name = name
        self.description = description
        self.reusable = reusable
        
    def describe(self):
        """Returns Description for Game."""
        print(self.name.title()+": "+self.description)


class HealthItem(Item):
    """Item that Affects player health."""

    def __init__(self, name, description, reusable, effect):
        Item.__init__(self, name, description, reusable)
        self.effect = effect

    def use(self, player):
        player.health += int(self.effect)
        print("Health Affected: "+str(self.effect))
        

class MessageItem(Item):
    """Item that only displays a message when used."""

    def __init__(self, name, description,reusable, message):
        Item.__init__(self, name, description, reusable)
        self.message = message

    def use(self, player):
        print(self.message)
        
        
