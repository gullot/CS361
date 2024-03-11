import tkinter as tk
from tkinter import ttk
from config import Config

def onEnter(event, trashButton, deleteHoverLabel):
    #to display information on hovering
    deleteHoverLabel.place(x=trashButton.winfo_rootx(), y=trashButton.winfo_rooty())

def onLeave(event, deleteHoverLabel):
    #remove hover label
    deleteHoverLabel.place_forget()

def onDarkModeClick(darkModeButton, addFlightButton):
    #global darkMode
    Config.darkMode = not Config.darkMode

    if Config.darkMode:
        Config.root.configure(bg="#2E2E2E")
        buttonColor = "#404040"
        textColor = "white"
        treeviewBg = "#1E1E1E"
        treeviewFg = "white"

    else:
        Config.root.configure(bg="white")
        buttonColor = "lightgray"
        textColor = "black"
        treeviewBg = "white"
        treeviewFg = "black"

    #update widget colors
    darkModeButton.configure(bg=buttonColor, fg=textColor)
    addFlightButton.configure(bg=buttonColor, fg=textColor)
    style = ttk.Style()
    style.configure("Custom.Treeview", background=treeviewBg, foreground=treeviewFg)  # Reconfigure Treeview style
    Config.root.update_idletasks()

def popUpErr(msg):
    popUp = tk.Toplevel()
    popUp.title("Error")
    label = tk.Label(popUp, text=msg)
    label.pack(padx=10, pady=10)
    button = tk.Button(popUp, text="OK", command=popUp.destroy)
    button.pack(pady=10)