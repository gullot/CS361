#creating a UI
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def onDarkModeClick():
    messagebox.showinfo("Clicked dark mode")

def onAddFlightClick():
    #open a new window
    flightWindow = tk.Toplevel(root)
    flightWindow.title("Add a Flight")
    flightWindow.geometry("200x100")

    label = tk.Label(flightWindow, text="Flight number: ")
    label.pack(padx=5, pady=5)

    flight = tk.Entry(flightWindow)
    flight.pack(padx=10, pady=10, anchor="center")

    submitFlight = tk.Button(flightWindow, text="Add Flight", command=lambda: addFlight(flightWindow, flight.get()))
    submitFlight.pack(pady=10)

def addFlight(window, flight):
    flightTable.insert("", tk.END, values=(flight, "", ""))
    window.destroy()

root = tk.Tk()
root.title("Welcome to the Flight Tracker Tool!")
root.geometry("1200x600")

trashIcon = tk.PhotoImage(file="./assets/trash.png")

darkModeButton = tk.Button(root, text="Dark Mode", command=onDarkModeClick)
darkModeButton.pack(padx=10, pady=10, anchor="nw")
addFlightButton = tk.Button(root, text="Add Flight", command=onAddFlightClick)
addFlightButton.pack(padx=10, pady=10, anchor="center")

flightTable = ttk.Treeview(root, columns=("Flight", "Arrival", "Departure", "Status", "Trash"), show="headings")
flightTable.heading("Flight", text="Flight", anchor=tk.CENTER)
flightTable.heading("Arrival", text="Arrival", anchor=tk.CENTER)
flightTable.heading("Departure", text="Departure", anchor=tk.CENTER)
flightTable.heading("Status", text="Status", anchor=tk.CENTER)
flightTable.heading("Trash", image=trashIcon, anchor=tk.CENTER)
flightTable.pack(padx=10, pady=10, anchor="center")


root.mainloop()