import db
import homePageController
import tripController

def getIndex():
    return homePageController.index()


def getTrips():
    return str(tripController.index())

def initAll():
    db.init()
    homePageController.init()
    tripController.init()