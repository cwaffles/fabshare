import requests
import subprocess

#server refers to mojio's api
apiURL = 'https://api.moj.io/v2/'
authToken = 'Bearer 70c22344-e864-45e1-be1c-8b20db5cfb39'

def getTrips():
    endpoint = 'trips'
    headers = {'Authorization': authToken}
    reqUrl = apiURL + endpoint
    print(reqUrl)
    return requests.get(reqUrl, headers=headers).content



def init():

    return 0