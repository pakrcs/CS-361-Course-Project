from flask import Flask, request, jsonify

app = Flask(__name__)

tour_averages = {
    "Driver": 282,
    "3 Wood": 249,
    "5 Wood": 236,
    "2 Iron": 231,
    "3 Iron": 218,
    "4 Iron": 209,
    "5 Iron": 199,
    "6 Iron": 188,
    "7 Iron": 176,
    "8 Iron": 164,
    "9 Iron": 152,
    "Pitching Wedge": 142
}

@app.route('/compare_distance', methods=['GET'])
def compare_distance():
    distance_str = request.args.get('distance')
    
    if distance_str is None or not distance_str.strip():
        return jsonify({"error": "Distance parameter is missing or empty"}), 400
    
    try:
        distance = float(distance_str)
    except ValueError:
        return jsonify({"error": "Invalid distance format"}), 400
    
    comparisons = {club: distance - avg_distance for club, avg_distance in tour_averages.items()}
    return jsonify(comparisons)

if __name__ == '__main__':
    app.run(port=5004)
