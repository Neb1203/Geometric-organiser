import tkinter
from tkinter import *
from tkinter import ttk
from StartScreenController import StartScreenController

root = Tk()
class StartScreen:
    startScreen = StartScreenController()

    root.title("Start Screen")

    # ttk.Button(mainframeStartscreen, text="play game", command=lambda: mainMenu.playGame()).grid(column=3, row=3, sticky=W)


    mainframeStartscreen = ttk.Frame(root, padding="100 100 100 100")
    mainframeStartscreen.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #start screen
    tkinter.Button(mainframeStartscreen, text="Go to Main Menu", command=lambda: StartScreenController.goToMainMenu()).grid(column=1, row=2, sticky=W)
    ttk.Button(mainframeStartscreen, text="Choose player profile", command=lambda: StartScreenController.pickPlayerProfile()).grid(column=1, row=3, sticky=W)
    ttk.Label(mainframeStartscreen, text="Geometric Organiser").grid(column=2, row=0, sticky=N)

    for child in mainframeStartscreen.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
