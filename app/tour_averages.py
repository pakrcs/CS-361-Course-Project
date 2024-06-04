from flask import Flask, request, jsonify

app = Flask(__name__)

tour_averages = {
    "Driver": 282.0,
    "3 Wood": 249.0,
    "5 Wood": 236.0,
    "2 Iron": 231.0,
    "3 Iron": 218.0,
    "4 Iron": 209.0,
    "5 Iron": 199.0,
    "6 Iron": 188.0,
    "7 Iron": 176.0,
    "8 Iron": 164.0,
    "9 Iron": 152.0,
    "Pitching Wedge": 142.0
}

@app.route('/compare_distance', methods=['GET'])
def compare_distance():
    club = request.args.get('club')
    distance_str = request.args.get('distance')
    
    if not club or club not in tour_averages:
        return jsonify({"error": "Club parameter is missing or invalid"}), 400
    
    if not distance_str or not distance_str.strip():
        return jsonify({"error": "Distance parameter is missing or empty"}), 400
    
    try:
        distance = float(distance_str)
    except ValueError:
        return jsonify({"error": "Invalid distance format"}), 400
    
    avg_distance = tour_averages[club]
    difference = distance - avg_distance
    comparison = "above" if difference > 0 else "below" if difference < 0 else "equal to"
    
    result = {
        "club": club,
        "entered_distance": distance,
        "tour_average_distance": avg_distance,
        "difference": abs(difference),
        "comparison": comparison
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5004)
