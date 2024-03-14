import json
from time import sleep
from config import Config
import tkinter as tk
from uiOperations import popUpErr, formatTime
import tkinter.messagebox as messagebox

def onAddFlightClick(flightTable):
    """opens a window for flight entry input"""
    flightWindow = tk.Toplevel(Config.root)
    flightWindow.title("Add a Flight")
    flightWindow.geometry("200x150")

    label = tk.Label(flightWindow, text="Please enter a flight number: ")
    label.pack(padx=5, pady=5)

    flight = tk.Entry(flightWindow)
    flight.pack(padx=10, pady=10, anchor="center")
    flight.focus_set()

    submitFlight = tk.Button(flightWindow, text="Add Flight", command=lambda: addFlight(flightWindow, flight.get(), flightTable))
    submitFlight.pack(pady=10)

def addFlight(window, flight, flightTable):
    """handles interaction with the flightaware microservice upon Add Flight click"""

    #send request to microservice for information regarding flight
    with open("request.txt", "w") as pipeRequest:
        pipeRequest.write(flight)

    sleep(3)

    arrival, departure, status = getRequest(window)

    flightTable.insert("", tk.END, values=(flight, arrival, departure, status))

    #close window
    window.destroy()

def deleteFlight(flightTable):
    """removes a selected flight from the table"""
    selected = flightTable.selection()
    result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected flight?")
    if result:
        if selected:
            flightTable.delete(selected)
        else:
            popUpErr("No flight selected to delete!")

def errorCheck(window):
    """performs error handling for the microservice response"""

    #help from https://www.geeksforgeeks.org/json-parsing-errors-in-python/
    with open("response.txt", "r") as flightDetails:
        try:
            data = json.load(flightDetails)
        except json.JSONDecodeError as e:
            popUpErr(e)
            window.destroy()
            return
    
    #check if microservice write "Error" as a key
    if "Error" in data:
        popUpErr("Error in return from API!")
        window.destroy()
        return
    
    #check if flights is empty (problem with retrieval)
    if not data["flights"]:
        popUpErr("No flight exists with the input number!")
        window.destroy()
        return
    
    return data

def getRequest(window):
    """retrieves the response from the microservice"""

    #perform error handling
    data = errorCheck(window)    

    #retrieve information
    arrival = data["flights"][0]["scheduled_in"]
    departure = data["flights"][0]["scheduled_out"]
    status = data["flights"][0]["status"]

    arrival = formatTime(arrival)
    departure = formatTime(departure)

    return arrival, departure, status