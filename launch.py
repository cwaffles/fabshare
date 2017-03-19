import rh
from flask import Flask

from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params




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

@app.route("/tripsCostPage/")
def blank():
    id = request.args.get('id', '')
    return rh.getTripPage(id)

#
# @app.route("/emailLoader/")
# def vehiclesIndex():
#     return rh.vehiclesIndex()
#



@app.before_first_request
def init():
    rh.initAll()

if __name__ == "__main__":
    app.run()

