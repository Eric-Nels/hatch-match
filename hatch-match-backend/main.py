from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from DB.suggestions import Suggestions

app = Flask(__name__)
CORS(app)

app.config['DATABASE'] = '/home/ericnels/Development/code/hatch-match/hatch-match-backend/hatch-match.db'

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/flies")
def get_flies():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT flies.name AS fly_name, 
                   flies.image AS fly_image, 
                   flies.type AS fly_type,
                   flies.imitation AS fly_imitation,
                   flies.life_cycle AS fly_life_cycle,
                   bugs.name AS bug_name, bugs.image AS bug_image
            FROM flies
            INNER JOIN bugs ON flies.imitation = bugs.name AND flies.life_cycle = bugs.life_cycle
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        data = [dict(row) for row in rows]

        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/submit", methods=['POST'])
def submit_suggestion():
    try:
        name = request.form['name']
        imitation = request.form['imitation']
        life_cycle = request.form['life_cycle']
        image = request.files['image'].read()

        suggestion = Suggestions(name=name, imitation=imitation, life_cycle=life_cycle, image=image)
        suggestion.save()

        return jsonify({"message": "Suggestion submitted successfully"})
    except Exception as e:
        app.logger.error("Error occurred while submitting suggestion: %s", str(e))
        return jsonify({"error": "An error occurred while submitting suggestion"}), 500


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=False)