#creating a UI
import tkinter as tk
from tkinter import ttk
from config import Config

from flightOperations import onAddFlightClick, deleteFlight, undoDelete
from uiOperations import onDarkModeClick, onEnter, onLeave

#dark mode off as default
darkMode = False
backgroundColor = "white"
buttonColor = "white"
textColor = "black"
treeviewBg = "white"
treeviewFg = "black"

#set up the main window
Config.root = tk.Tk()
Config.root.configure(bg="white")
Config.root.title("Welcome to the Flight Tracker Tool!")
titleFrame = tk.Frame(Config.root)
titleFrame.pack(pady=10)
titleLabel = tk.Label(titleFrame, text="Click or hover over the buttons below to get started!", bg=backgroundColor)
titleLabel.pack()
Config.root.geometry("900x500")

#button set up
buttonFrame = tk.Frame(Config.root, bg=backgroundColor)
buttonFrame.pack(padx=10, pady=10, anchor="center")

addFlightButton = tk.Button(buttonFrame, text="Add Flight", bg=backgroundColor, fg=textColor)
addFlightButton.config(command=lambda: onAddFlightClick(flightTable))
addFlightButton.pack(side=tk.LEFT)

trashIcon = tk.PhotoImage(file="./assets/trash.png")
trashButton = tk.Button(buttonFrame, image=trashIcon, command=lambda: deleteFlight(flightTable))
deleteHoverLabel = tk.Label(Config.root, text="warning! this will delete a flight")
trashButton.pack(side=tk.LEFT, padx=10)
trashButton.bind("<Enter>", lambda event: onEnter(event, trashButton, deleteHoverLabel))
trashButton.bind("<Leave>", lambda event: onLeave(event, deleteHoverLabel))

undoButton = tk.Button(buttonFrame, text="Undo Delete", bg=backgroundColor, fg=textColor)
undoButton.config(command=lambda: undoDelete(flightTable))
undoButton.pack(side=tk.LEFT, padx=5)

darkModeButton = tk.Button(Config.root, text="Toggle Dark Mode", bg=backgroundColor, fg=textColor)
darkModeButton.config(command=lambda: onDarkModeClick(darkModeButton, addFlightButton, trashButton, titleLabel, buttonFrame, undoButton))
darkModeButton.pack(padx=10, pady=10, anchor="nw")

#set up the table
style = ttk.Style()
style.configure("Custom.Treeview", background=treeviewBg, foreground=treeviewFg)
flightTable = ttk.Treeview(Config.root, columns=("Flight", "Arrival", "Departure", "Status"), show="headings", style="Custom.Treeview")
flightTable.heading("Flight", text="Flight", anchor=tk.CENTER)
flightTable.heading("Arrival", text="Arrival", anchor=tk.CENTER)
flightTable.heading("Departure", text="Departure", anchor=tk.CENTER)
flightTable.heading("Status", text="Status", anchor=tk.CENTER)
flightTable.pack(padx=10, pady=10, anchor="center")

#run UI
Config.root.mainloop()