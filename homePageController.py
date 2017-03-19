import requests
import json

#custom stuff
import globals
import db

def index():
    # getTrips()
    return "<html><title></title><body><p>Hello World!</p></body></html>"

#Loads summary trip info from Mojio, returns 2d array (list) with summary data by trip
def loader():
    tripsJSON = getAllTrips()
    print(tripsJSON)
    allRelData = [] #list for final storage of all relevant data
    for trip in tripsJSON["Data"]:
        #Trip ID // Start City // End City // Start Timestamp // Distance[m] // Fuel Efficiency[km/L]// Vehicle ID
        relevantDataList = [trip["Id"],
                            trip["StartLocation"]["Address"]["City"],
                            trip["EndLocation"]["Address"]["City"],
                            trip["StartTimestamp"],
                            trip["Distance"]["Value"],
                            trip["FuelEfficiency"]["Value"],
                            trip["VehicleId"]]
        allRelData.append(relevantDataList)
    return allRelData

def getFromAPI(url):
    headers = {'Authorization': globals.authToken}
    # print(url)
    return requests.get(url, headers=headers).content

def getAllTrips():
    endpoint = 'trips'
    url = globals.apiURL + endpoint
    response = json.loads(getFromAPI(url))
    return response

def getEvents(tripID):
    url = globals.apiURL + 'trips/' + tripID + '/history/states?top=9999'
    response = json.loads(getFromAPI(url))
    print(type(response))
    return response



def init():
    #do all the data loading here
    return #stub