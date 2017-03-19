import db
import homePageController
import tripsController
import vehiclesController


def initAll():
    db.init()
    homePageController.init()
    tripsController.init()
    vehiclesController.init()

def getIndex():
    return homePageController.index()

def tripsIndex():
    return tripsController.index()

def getTrips():
    return str(tripsController.index())

def vehiclesIndex():
    return vehiclesController.index()

def shutdownAll():
    return
