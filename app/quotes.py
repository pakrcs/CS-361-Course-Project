from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/get_quote')
def get_quote():
    with open('golf_quotes.txt', 'r') as file:
        quotes = file.readlines()
    random_quote = random.choice(quotes).strip()
    return jsonify({"quote": random_quote})


if __name__ == "__main__":
    app.run(port=5002)