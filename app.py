from flask import Flask, jsonify
from entities.trip import Trip

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return jsonify({"succes": True, 
                    "message":"Hello World"}), 200


@app.route('/trips',methods=["GET"])
def trips():
    trips = Trip.getAll()
    return trips

if __name__ == "__main__":
    app.run()