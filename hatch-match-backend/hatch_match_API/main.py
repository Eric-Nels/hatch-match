from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

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
    cursor.execute('SELECT flies.id, flies.name, flies.image, fly_types.type, species.name AS species_name FROM flies JOIN fly_types ON flies.type_id = fly_types.type_id JOIN species ON flies.species_id = species.species_id;')
    rows = cursor.fetchall()

    data = [dict(row) for row in rows]

    conn.close()
    return jsonify(data)    


if __name__ == "__main__":
    app.run(debug=True)