import requests
import json
import subprocess

#server refers to mojio's api
apiURL = 'https://api.moj.io/v2/'
authToken = 'Bearer 70c22344-e864-45e1-be1c-8b20db5cfb39'



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
    return response




def init():

    return 0