from flask import Flask, request, jsonify

app = Flask(__name__)

goals = []

@app.route('/submit_goal', methods=['POST'])
def submit_goal():
    goal_text = request.json.get('goal')
    if goal_text:
        goals.append(goal_text)
        response = {'message': f'Goal "{goal_text}" submitted successfully'}
        return jsonify(response), 200
    else:
        response = {'error': 'Please provide a valid goal'}
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(port=5005)
