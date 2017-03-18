import requests
import subprocess

nodeURL = 'http://localhost'
nodePort = 4321

def getTrips():
    address = nodeURL + ':' + str(nodePort) + '/'
    print(address)
    return requests.get(address).content


def init():

    return 0