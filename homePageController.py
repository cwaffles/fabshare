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
    insertDummyEmail(userEmail)
    insertDummyVehicles(filteredTrips, userEmail)
    insertTuples(filteredTrips, userEmail)
    return

def insertDummyEmail(userEmail):
    cur = globals.__conn.cursor()

    # string = "INSERT INTO human (email) VALUES ('test@test.com')"
    # cur.execute(string)
    cur.execute("INSERT INTO human (email) VALUES (%s)", (userEmail,)) #super hacky

    globals.__conn.commit()
    cur.close()
    return

def insertDummyVehicles(filteredTrips, userEmail):
    cur = globals.__conn.cursor()

    vidList = set()
    for trip in filteredTrips:
        vidList.add(trip["vid"])

    for vid in vidList:
        print("%s %s" % (vid, userEmail))
        cur.execute("INSERT INTO vehicle (vid, email) VALUES (%s, %s)", (vid, userEmail))

    globals.__conn.commit()
    cur.close()
    return

def insertTuples(filteredTrips, userEmail):
    cur = globals.__conn.cursor()

    #   tid   VARCHAR(64) PRIMARY KEY,
    #   vid   VARCHAR(64) REFERENCES vehicle (vid),
    #   email VARCHAR(64) REFERENCES human (email),
    #   startCity VARCHAR(64),
    #   endCity VARCHAR(64),
    #   distance REAL,
    #   efficiency REAL,
    #   date TIMESTAMP

    for trip in filteredTrips:
        print( "%s, %s, %s, %s, %s, %s, %s, %s)",
        (trip["tid"], trip["vid"], userEmail, trip["startCity"], trip["endCity"],
         trip["distance"], trip["efficiency"], trip["startTimestamp"]))

        cur.execute("INSERT INTO trip (tid, vid, email, startCity, endCity, distance, efficiency, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (trip["tid"], trip["vid"], userEmail, trip["startCity"], trip["endCity"], trip["distance"], trip["efficiency"], trip["startTimestamp"]))


    globals.__conn.commit()
    cur.close()
    return