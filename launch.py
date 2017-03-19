import db
import rh
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return rh.getIndex()


@app.route("/vehicles/")
def vehiclesIndex():
    return "Vehicles homepage"

@app.before_first_request
def init():
    rh.initAll()

if __name__ == "__main__":
    app.run()

