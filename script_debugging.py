import rh
import views
import ipdb
from flask import Flask
app = Flask(__name__)

rh.sendEmail("Cash for dash!", "joren.Jackson@gmail.com", 14, 5.66, "K. Fab")

gasPrice = views.getGasPrice("V4L2H3")
print(gasPrice)

trips = rh.loader()
Home = views.generateHomePage(trips)
Home = views.generateTripPage(trips[0])
#Home = views.generateRequestMoneyPage(trips[0])

#myTrip = 0
#fuelConsumed = trips['Data'][myTrip]['StartFuelLevel']['Value'] - trips['Data'][0]['EndFuelLevel']['Value']

rh.getEvents('dfa04b28-3882-49a9-8cb6-8fd6f6163885')



# ipdb.set_trace() #for debug
#print(rh.nodePort)


initialized = False

@app.route("/")
def hello():
    return Home

if __name__ == "__main__":
    app.run()
