import tkinter
from tkinter import *
from tkinter import ttk
from MainMenuController import MainMenuController

root = Tk()
class MainMenu:
    mainMenu = MainMenu()

    root.title("Main menu")

    mainframeMainMenu = ttk.Frame(root, padding="100 100 100 100")
    mainframeMainMenu.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #mainMenu
    tkinter.Button(mainframeMainMenu, text="Play", command=lambda: MainMenu.play()).grid(column=1, row=1, sticky=N)
    ttk.Button(mainframeMainMenu, text="Profile", command=lambda: MainMenu.profile()).grid(column=1, row=2, sticky=N)
    ttk.Button(mainframeMainMenu, text="How to play?", command=lambda: MainMenu.howToPlay()).grid(column=1, row=3, sticky=N)
    ttk.Button(mainframeMainMenu, text="Back", command=lambda: MainMenu.back()).grid(column=1, row=4, sticky=N)
    ttk.Button(mainframeMainMenu, text="Settings", command=lambda: MainMenu.settings()).grid(column=1, row=5, sticky=N)
    ttk.Label(mainframeMainMenu, text="Geometric Organiser").grid(column=1, row=0, sticky=N)

    for child in mainframeMainMenu.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()