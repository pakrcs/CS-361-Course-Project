from flask import Flask, request, jsonify

app = Flask(__name__)


def get_club_recommendation(distance, wind_condition):
    print(f"Received distance: {distance}, wind_condition: {wind_condition}")

    if wind_condition == "Downwind":
        distance *= 0.95
    elif wind_condition == "Into the Wind":
        distance *= 1.05
    elif wind_condition == "None":
        distance *= 1

    print(f"Adjusted distance: {distance}")

    if distance > 250:
        return "Driver"
    elif distance > 225:
        return "3 Wood"
    elif distance > 210:
        return "5 Wood"
    elif distance > 200:
        return "2 Iron"
    elif distance > 190:
        return "3 Iron"
    elif distance > 180:
        return "4 Iron"
    elif distance > 170:
        return "5 Iron"
    elif distance > 160:
        return "6 Iron"
    elif distance > 150:
        return "7 Iron"
    elif distance > 140:
        return "8 Iron"
    elif distance > 130:
        return "9 Iron"
    elif distance > 120:
        return "Pitching Wedge"
    elif distance > 105:
        return "Gap Wedge"
    elif distance > 100:
        return "52° Wedge"
    elif distance > 90:
        return "56° Wedge"
    else:
        return "60° Wedge"


@app.route('/recommend_club', methods=['GET'])
def recommend_club():
    distance = float(request.args.get('distance'))
    wind_condition = request.args.get('wind_condition')
    recommendation = get_club_recommendation(distance, wind_condition)
    print(f"Recommended club: {recommendation}")
    return jsonify({"recommended_club": recommendation})


if __name__ == "__main__":
    app.run(port=5003)
