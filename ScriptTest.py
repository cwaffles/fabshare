import homePageController
import globals
import db
db.init()
homePageController.loadTripsIntoDB("a@a.com")

print(homePageController.getTripSummaries("a@a.com"))

