from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/word")
def get_word():
    with open("data/anki_deck.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    random_row = random.choice(rows)
    return random_row

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
