#GUI for adventure game
from tkinter import*

class Interface():
    """User Interface for creating a text adventure."""

    def __init__(self):

        self.root = Tk()
        self.root.title('Text Adventure Engine'+'\n' * 12)
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.home()
        self.root.mainloop()
    def home(self):
    
        
        #Main Frame

        self.main_frame = Frame(self.root)
        self.main_frame.pack()
        self.header = Label(self.main_frame,
                            text="\nTEXT ADVENTURE ENGINE" + "\n"*8,
                            font = ("Elephant", 16),
                            ).pack(side="top")

        self.location_button = Button(self.main_frame,
                                      text="Create Location",
                                      font="Elephant",
                                      command = self.make_location
                                      ).pack(side="left", padx = 5)

        self.npc_button = Button(self.main_frame,
                                text="Create NPC",
                                font="Elephant",
                                command=self.make_npc
                                 ).pack(side="left", padx=5)

        self.item_button = Button(self.main_frame,
                                text="Create Item",
                                font="Elephant",
                                command=self.make_item
                                  ).pack(side="left", padx=5)
                

        
        #self.root.mainloop()




    def make_location(self):
        """New Location Form"""
        self.main_frame.pack_forget()
        #Location Frame
        
        self.location_frame = Frame(self.root)
        self.location_header = Label(self.location_frame,
                                     text="NEW LOCATION\n\n",
                                     font= ("Elephant", 20)
                                     ).pack(side="top")
                                     
        self.location_name_label = Label(self.location_frame,
                                         text = "Location Name:"
                                         ).pack(side="left")
        self.location_name_entry = Entry(self.location_frame)
        self.location_name_entry.pack(side="right")
        self.location_frame2 = Frame(self.root)
        self.location_id_label = Label(self.location_frame2,
                                       text="ID #" + " "*72,
                                       ).pack(side="left")
        self.location_id_entry = Entry(self.location_frame2,
                                       width=3)
        self.location_id_entry.pack(side="right")
        self.location_frame3 = Frame(self.root)
        self.location_description_label = Label(self.location_frame3,
                                                text="Description" + " "*67
                                                ).pack()
        self.location_description_entry = Text(self.location_frame3,
                                               height=16,
                                               width=60)
        self.location_description_entry.pack()
        self.location_frame4 = Frame(self.root)
        self.cancel = Button(self.location_frame4,
                             text="CANCEL",
                             command=self.cancel_location
                             ).pack(side="left")
        self.next = Button(self.location_frame4,
                           text = "NEXT",
                           command=self.make_location2
                           ).pack(side="right")
        self.location_frames = [self.location_frame,
                                self.location_frame2,
                                self.location_frame3,
                                self.location_frame4]
        for frame in self.location_frames:
            frame.pack()
        

    def make_location2(self):
        for frame in self.location_frames:
            frame.pack_forget()

        

    def cancel_location(self):
        self.location_frame.pack_forget()
        self.location_frame2.pack_forget()
        self.location_frame3.pack_forget()
        self.location_frame4.pack_forget()
        self.home()

    def make_npc(self):
        pass

    def make_item(self):
        pass



gui = Interface()
