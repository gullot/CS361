#creating a UI
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#########################################################

def onDarkModeClick():
    #messagebox.showinfo("Clicked dark mode")
    global darkMode
    darkMode = not darkMode

    if darkMode:
        root.configure(bg="#2E2E2E")
        #buttonColor = "#404040"
        #textColor = "white"

    else:
        root.configure(bg="white")
        #buttonColor = "lightgray"
        #textColor = "black"

    #update widget colors
    #darkModeButton.configure(bg=buttonColor, fg=textColor)
    #flightTable.configure(style="Treeview", background=root.cget("bg"), foreground=textColor, fieldbackground=root.cget("bg"))
    

def onAddFlightClick():
    #open a new window
    flightWindow = tk.Toplevel(root)
    flightWindow.title("Add a Flight")
    flightWindow.geometry("200x150")

    label = tk.Label(flightWindow, text="Flight number: ")
    label.pack(padx=5, pady=5)

    flight = tk.Entry(flightWindow)
    flight.pack(padx=10, pady=10, anchor="center")
    flight.focus_set()

    submitFlight = tk.Button(flightWindow, text="Add Flight", command=lambda: addFlight(flightWindow, flight.get()))
    submitFlight.pack(pady=10)

def addFlight(window, flight):
    flightTable.insert("", tk.END, values=(flight, "13:00", "18:00"))
    #close window
    window.destroy()

#########################################################################

root = tk.Tk()
root.title("Welcome to the Flight Tracker Tool!")
root.geometry("1200x600")

#dark mode off as default
darkMode = False
backgroundColor = "white"
buttonColor = "lightgray"
textColor = "black"

trashIcon = tk.PhotoImage(file="./assets/trash.png")

darkModeButton = tk.Button(root, text="Dark Mode", command=onDarkModeClick, bg=backgroundColor, fg=textColor)
darkModeButton.pack(padx=10, pady=10, anchor="nw")
addFlightButton = tk.Button(root, text="Add Flight", command=onAddFlightClick, bg=backgroundColor, fg=textColor)
addFlightButton.pack(padx=10, pady=10, anchor="center")

flightTable = ttk.Treeview(root, columns=("Flight", "Arrival", "Departure", "Status", "Trash"), show="headings", style="Treeview")
flightTable.heading("Flight", text="Flight", anchor=tk.CENTER)
flightTable.heading("Arrival", text="Arrival", anchor=tk.CENTER)
flightTable.heading("Departure", text="Departure", anchor=tk.CENTER)
flightTable.heading("Status", text="Status", anchor=tk.CENTER)
flightTable.heading("Trash", image=trashIcon, anchor=tk.CENTER)
flightTable.pack(padx=10, pady=10, anchor="center")

style = ttk.Style()
style.configure("Treeview", background=root.cget("bg"), foreground=textColor, fieldbackground=root.cget("bg"), rowheight=25)

root.mainloop()