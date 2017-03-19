import db
import homePageController
import tripsController
import vehiclesController

def getIndex():
    return homePageController.index()

def tripsIndex():
    return tripsController.index()

def vehiclesIndex():
    return vehiclesController.index()

def getTrips():
    return str(tripsController.index())

def initAll():
    db.init()
    homePageController.init()
    tripsController.init()