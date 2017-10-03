from tkinter import Tk, Label, Button, messagebox
import random

rickyism = ["Fuck you, Lahey!", "allow me to play doubles advocate here for a moment. ",
            "For all intensive purposes I think you are wrong.",
            "you all seem to be taking something very valuable for granite.",
            "Gettin' two birds stoned at once",
            "Keep your friends close but your enemies toaster.",
            "It would be my pleasurement",
            "Baste yourself, boys. I'm going to Toronto to become a street person.",
            "Storming the jungles at Normanly",
            "I'll do some fuckin weiner work for that kind of money",
            "Jacob's not the smartest knife in the drawer you guys",
            "A link is only as long as your longest strong chain",
            "Cock-a-doodle Fucking Ketchup Chips",
            "Does a bear shit on the pope?",
            "Fire Retarded",
            "Friends with the Benedicts",
            "Good things come to those at the gate",
            "I dont have enough people words to make it understand you the way it understands me",
            "It's clear to see who makes the pants here",
            ]
class RickyGUI:

    def __init__(self, master):
        self.master = master
        master.title("Ricky GUI")

        self.label = Label(master, text="Click 'Fuck Off' for Rickyisms")
        self.label.pack()

        self.greet_button = Button(master, text="Fuck Off", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def greet(self):
        messagebox.showinfo("Rickyism", random.choice(rickyism))

root = Tk()
my_gui = RickyGUI(root)
root.mainloop()