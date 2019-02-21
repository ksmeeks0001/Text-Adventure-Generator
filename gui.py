#GUI for adventure game
from tkinter import*

class Interface():
    """User Interface for creating a text adventure."""

    def __init__(self):

        self.root = Tk()
        self.root.title('Text Adventure Engine'+'\n' * 12)
        self.root.geometry("500x500")
        #Main Frame
        self.mainframe = Frame(self.root)
        self.header = Label(self.mainframe,
                            text="TEXT ADVENTURE ENGINE",
                            font = "CASTELLAR" )

        self.location_button = Button(self.mainframe,
                                      text="Create Location",
                                      font="Elephant",
                                      command = self.make_location)
        

        #pack Main Frame
        self.mainframe.pack()
        self.header.pack()
        self.location_button.pack(side='bottom')





    def make_location(self):
        pass







        
        

        self.root.mainloop()

gui = Interface()
