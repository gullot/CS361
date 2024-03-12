#creating a UI
import tkinter as tk
from tkinter import ttk
from config import Config

from flightOperations import onAddFlightClick, deleteFlight
from uiOperations import onDarkModeClick, onEnter, onLeave

#########################################################################

Config.root = tk.Tk()
Config.root.configure(bg="white")
Config.root.title("Welcome to the Flight Tracker Tool!")
titleFrame = tk.Frame(Config.root)
titleFrame.pack(pady=10)
titleLabel = tk.Label(titleFrame, text="Click the buttons below to get started!")
titleLabel.pack()
Config.root.geometry("1200x600")

#dark mode off as default
darkMode = False
backgroundColor = "white"
buttonColor = "lightgray"
textColor = "black"
treeviewBg = "white"
treeviewFg = "black"

trashIcon = tk.PhotoImage(file="./assets/trash.png")
trashButton = tk.Button(Config.root, image=trashIcon, command=lambda: deleteFlight(flightTable))

deleteHoverLabel = tk.Label(Config.root, text="warning! this will delete a flight")
trashButton.pack()
trashButton.bind("<Enter>", lambda event: onEnter(event, trashButton, deleteHoverLabel))
trashButton.bind("<Leave>", lambda event: onLeave(event, deleteHoverLabel))

darkModeButton = tk.Button(Config.root, text="Dark Mode", bg=backgroundColor, fg=textColor)
darkModeButton.config(command=lambda: onDarkModeClick(darkModeButton, addFlightButton))
darkModeButton.pack(padx=10, pady=10, anchor="nw")

addFlightButton = tk.Button(Config.root, text="Add Flight", bg=backgroundColor, fg=textColor)
addFlightButton.config(command=lambda: onAddFlightClick(flightTable))
addFlightButton.pack(padx=10, pady=10, anchor="center")

style = ttk.Style()
#style.configure("Treeview", background=root.cget("bg"), foreground=textColor, fieldbackground=root.cget("bg"), rowheight=25)
style.configure("Custom.Treeview", background=treeviewBg, foreground=treeviewFg)

flightTable = ttk.Treeview(Config.root, columns=("Flight", "Arrival", "Departure", "Status"), show="headings", style="Custom.Treeview")
flightTable.heading("Flight", text="Flight", anchor=tk.CENTER)
flightTable.heading("Arrival", text="Arrival", anchor=tk.CENTER)
flightTable.heading("Departure", text="Departure", anchor=tk.CENTER)
flightTable.heading("Status", text="Status", anchor=tk.CENTER)
flightTable.pack(padx=10, pady=10, anchor="center")

Config.root.mainloop()