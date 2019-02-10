#GUI for adventure game
from tkinter import*
class Gui():
    """Gui shows player stats for adventure game."""

    def __init__(self):
        #initialize
        self.root = Tk()
        self.root.configure(background = 'red')
        self.root.title('ADVENTURE')
        #frames
        self.left = Frame(self.root)
        self.left.configure(background = 'red')
        self.right = Frame(self.root)

        #left side labels
        self.health = Label(self.left, text= 'Health',
                            background = 'red')
        self.equiped = Label(self.left, text = 'Equiped',
                             background = 'red')
        self.inventory = Label(self.left, text = 'Inventory',
                               background = 'red')

        #pack left
        self.health.pack()
        self.equiped.pack()
        self.inventory.pack()
        self.left.pack(side = LEFT)

        self.root.mainloop()
gui = Gui()
