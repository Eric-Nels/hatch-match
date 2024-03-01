from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import base64
from DB.suggestions import Suggestions

app = Flask(__name__)
CORS(app)

app.config['DATABASE'] = '/home/ericnels/Development/code/hatch-match/hatch-match-backend/hatch-match.db'

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/data")
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT flies.name AS fly_name, 
               flies.image AS fly_image, 
               flies.type AS fly_type,
               flies.imitation AS fly_imitation,
               flies.life_cycle AS fly_life_cycle
        FROM flies
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    data = [dict(row) for row in rows]

    conn.close()
    return jsonify(data)

@app.route("/api/submit", methods=['POST'])
def submit_suggestion():
    name = request.form['name']
    image = request.files['image'].read()

    suggestion = Suggestions(name=name, image=image)
    suggestion.save()

    return jsonify({"message": "Suggestion submitted successfully"})   


if __name__ == "__main__":
    app.run(debug=False)