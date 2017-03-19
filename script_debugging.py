import rh
import ipdb
from flask import Flask
app = Flask(__name__)


trips = rh.loader()

rh.getEvents('dfa04b28-3882-49a9-8cb6-8fd6f6163885')



# ipdb.set_trace() #for debug
#print(rh.nodePort)


initialized = False

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
