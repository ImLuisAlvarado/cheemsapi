from flask import Flask, request, jsonify
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

@app.route('/trip', methods=['POST'])
def save_trip():
    data = request.json
    trip = Trip(name=data['name'], 
                city=data['city'],
                latitude=data['latitude'],
                longitude=data['longitude'])
    
    id = trip.save()
    success = id is not None
    return jsonify(success), 201

if __name__ == "__main__":
    app.run()