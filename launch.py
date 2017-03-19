import rh
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def testDB():
    return str(rh.getTestData())

@app.route("/vehicles/")
def vehiclesIndex():
    return "Vehicles homepage"

@app.before_first_request
def init():
    rh.init()

if __name__ == "__main__":
    app.run()

