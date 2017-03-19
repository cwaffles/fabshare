import requests
import json
import subprocess

#server refers to mojio's api
apiURL = 'https://api.moj.io/v2/'
authToken = 'Bearer f39d6d3f-9785-44bb-a9f8-65cb2b8fd338'


#Loads summary trip info from Mojio, returns 2d array (list) with summary data by trip
def loader():
    tripsJSON = getAllTrips()
    print(tripsJSON)
    allRelData = [] #list for final storage of all relevant data
    for trip in tripsJSON["Data"]:
        #Trip ID // Start City // End City // Start Timestamp // Distance[m] // Fuel Efficiency[km/L]// Vehicle ID
        #Exceptions for if no usable address data
        try:
            StartLocation = trip["StartLocation"]["Address"]["City"]
        except:
            StartLocation = "Somewhere"
        try:
            EndLocation = trip["EndLocation"]["Address"]["City"]
        except:
            EndLocation = "Somewhere"

        relevantDataList = [trip["Id"],
                            StartLocation,
                            EndLocation,
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

def sendEmail(emailadd, fuelUsed, costEst, personName):
    import email
    import smtplib
    from jinja2 import Template

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("dividfabshare@gmail.com", "fabshare")

    msg = "Hey there freeloader,\n\nMY CAR RUNS ON FUEL NOT FRIENDSHIP!\n I used {{gasamount}} liters of fuel so you part is {{Money}}$\n\n" \
          "your obedient servant,\n" \
          "{{userName}}"

    t = Template(msg)
    output = t.render(gasamount = fuelUsed, Money = costEst, userName = personName)
    server.sendmail("dividfabshare@gmail.com", emailadd, output)
    server.quit()