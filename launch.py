# from .rh import *
import rh
import ipdb
from flask import Flask
app = Flask(__name__)






# ipdb.set_trace() #for debug
print(rh.nodePort)


initialized = False

@app.route("/")
#def hello():
 #   return "Hello World!"

if __name__ == "__main__":
    app.run()

