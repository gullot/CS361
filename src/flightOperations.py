import json
from time import sleep
from config import Config
import tkinter as tk
from uiOperations import popUpErr

def onAddFlightClick():
    #open a new window
    flightWindow = tk.Toplevel(Config.root)
    flightWindow.title("Add a Flight")
    flightWindow.geometry("200x150")

    label = tk.Label(flightWindow, text="Flight number: ")
    label.pack(padx=5, pady=5)

    flight = tk.Entry(flightWindow)
    flight.pack(padx=10, pady=10, anchor="center")
    flight.focus_set()

    submitFlight = tk.Button(flightWindow, text="Add Flight", command=lambda: addFlight(flightWindow, flight.get()))
    submitFlight.pack(pady=10)

def addFlight(window, flight, flightTable):

    #send request to microservice for information regarding flight
    with open("request.txt", "w") as pipeRequest:
        pipeRequest.write(flight)

    sleep(3)

    #help from https://www.geeksforgeeks.org/json-parsing-errors-in-python/
    with open("response.txt", "r") as flightDetails:
        try:
            data = json.load(flightDetails)
        except json.JSONDecodeError as e:
            popUpErr(e)
            #print("inval syntax:", e)
            window.destroy()
            return
    
    #check if microservice write "Error" as a key
    if "Error" in data:
        #print("error in return from api")
        popUpErr("Error in return from API")
        window.destroy()
        return
    
    #check if flights is empty (problem with retrieval)
    if not data["flights"]:
        #print("no data in flights key")
        popUpErr("No data in flights key")
        window.destroy()
        return

    arrival = data["flights"][0]["scheduled_in"]
    departure = data["flights"][0]["scheduled_out"]
    status = data["flights"][0]["status"]

    flightTable.insert("", tk.END, values=(flight, arrival, departure, status)) #still need to add delete button in last column

    #close window
    window.destroy()

def onDeleteFlightClick(row, flightTable):
    flightTable.delete(row)