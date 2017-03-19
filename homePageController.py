import requests
import json

#custom stuff
import globals
import db

def index():
    # getTrips()
    return "<html><title></title><body><p>Hello World!</p></body></html>"

def init():
    #do all the data loading here
    loadTripsIntoDB("test@test.com")
    return #stub

#helper function to make http request
def getFromAPI(url):
    headers = {'Authorization': globals.authToken}
    return requests.get(url, headers=headers).content

#returns raw unfiltered trips
def getUnfilteredTrips():
    endpoint = 'trips'
    url = globals.apiURL + endpoint
    response = json.loads(getFromAPI(url))
    return response

#Loads summary trip info from Mojio, returns 2d array (list) with summary data by trip
def getFilteredTrips(tripsJSON):
    # print(tripsJSON)
    allRelData = [] #list for final storage of all relevant data
    print(tripsJSON)
    for trip in tripsJSON["Data"]:
        #Trip ID // Start City // End City // Start Timestamp // Distance[m] // Fuel Efficiency[km/L]// Vehicle ID
        try:
            relevantDataList = {"tid":              trip["Id"],
                                "startCity":        trip["StartLocation"]["Address"]["City"],
                                "endCity":          trip["EndLocation"]["Address"]["City"],
                                "startTimestamp":   trip["StartTimestamp"],
                                "distance":         trip["Distance"]["Value"],
                                "efficiency":       trip["FuelEfficiency"]["Value"],
                                "vid":              trip["VehicleId"]}
            allRelData.append(relevantDataList)
        except:
            relevantDataList = {"tid": trip["Id"],
                                "startCity": "...",
                                "endCity": "...",
                                "startTimestamp": trip["StartTimestamp"],
                                "distance": trip["Distance"]["Value"],
                                "efficiency": trip["FuelEfficiency"]["Value"],
                                "vid": trip["VehicleId"]}
            allRelData.append(relevantDataList)

    return allRelData

#unused at the moment
def getEvents(tripID):
    url = globals.apiURL + 'trips/' + tripID + '/history/states?top=9999'
    response = json.loads(getFromAPI(url))
    # print(type(response))
    return response

def loadTripsIntoDB(userEmail):
    unfilteredTrips = getUnfilteredTrips()
    filteredTrips = getFilteredTrips(unfilteredTrips)
    db.insertEmail(userEmail)
    db.insertVehicles(filteredTrips, userEmail)
    db.insertTrips(filteredTrips, userEmail)
    return

