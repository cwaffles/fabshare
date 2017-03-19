import requests
import json
import subprocess

#server refers to mojio's api
apiURL = 'https://api.moj.io/v2/'
authToken = 'Bearer 70c22344-e864-45e1-be1c-8b20db5cfb39'


#Loads summary trip info from Mojio, returns 2d array (list) with summary data by trip
def loader():
    tripsJSON = getAllTrips()
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
    return(allRelData)

def getFromAPI(url):
    headers = {'Authorization': authToken}
    print(url)
    return requests.get(url, headers=headers).content

def getAllTrips():
    endpoint = 'trips'
    url = apiURL + endpoint
    response = json.loads(getFromAPI(url))
    return response

def getEvents(tripID):
    url = apiURL + 'trips/' + tripID + '/history/states?top=9999'
    response = json.loads(getFromAPI(url))
    print(type(response))
    return response

def init():

    return 0