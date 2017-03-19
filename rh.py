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

def getTripPage(id):
    return tripsController.index(id)

def getTrips():
    return str(tripsController.index())

def vehiclesIndex():
    return vehiclesController.index()

