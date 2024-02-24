#creating a UI
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from time import sleep
import json

#########################################################

def onEnter(event):
    #to display information on hovering
    deleteHoverLabel.place(x=trashButton.winfo_rootx(), y=trashButton.winfo_rooty())

def onLeave(event):
    #remove hover label
    deleteHoverLabel.place_forget()

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

    #ADD PIPE REQUEST HERE
    with open("request.txt", "w") as pipeRequest:
        pipeRequest.write(flight)

    sleep(2)

    with open("response.txt", "r") as flightDetails:
        data = json.load(flightDetails)

    arrival = data['predicted_in']
    departure = data['predicted_out']
    status = data['status']


    flightTable.insert("", tk.END, values=(flight, arrival, departure, status)) #sstill need to add delete button in last column
    #close window
    window.destroy()

#########################################################################

root = tk.Tk()
root.title("Welcome to the Flight Tracker Tool!")
titleFrame = tk.Frame(root)
titleFrame.pack(pady=10)
titleLabel = tk.Label(titleFrame, text="Click the buttons below to get started!")
titleLabel.pack()
root.geometry("1200x600")

#dark mode off as default
darkMode = False
backgroundColor = "white"
buttonColor = "lightgray"
textColor = "black"

trashIcon = tk.PhotoImage(file="./assets/trash.png")
trashButton = tk.Button(root, image=trashIcon)

deleteHoverLabel = tk.Label(root, text="warning! this will delete a flight")
trashButton.pack()
trashButton.bind("<Enter>", onEnter)
trashButton.bind("<Leave>", onLeave)

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