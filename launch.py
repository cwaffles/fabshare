import rh
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return rh.getIndex()

@app.route("/trips/")
def tripsIndex():
    return rh.tripsIndex()

@app.route("/vehicles/")
def vehiclesIndex():
    return rh.vehiclesIndex()


@app.route("/vehicles/")
def vehiclesIndex():
    return rh.vehiclesIndex()

@app.before_first_request
def init():
    rh.initAll()

if __name__ == "__main__":
    app.run()