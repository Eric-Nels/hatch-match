from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from DB.catch_of_week import Catch_of_week
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
            SELECT flies.fly_id AS fly_id,
                   flies.name AS fly_name, 
                   flies.image AS fly_image, 
                   flies.type AS fly_type,
                   flies.imitation AS fly_imitation,
                   flies.life_cycle AS fly_life_cycle,
                   flies.materials AS fly_materials,
                   flies.instructions AS fly_instructions,
                   bugs.name AS bug_name, 
                   bugs.image AS bug_image
            FROM flies
            INNER JOIN bugs ON flies.imitation = bugs.name AND flies.life_cycle = bugs.life_cycle
            ORDER BY fly_name
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
    

@app.route("/api/catch_of_week", methods=['POST'])
def submit_catch_of_week():
    try:
        
        catch_image = request.files['catch_image'].read()
        social = request.form['social']

        catch_of_week = Catch_of_week(catch_image=catch_image, social=social)
        catch_of_week.save()

        return jsonify({"message": "Catch submitted successfully"})
    except Exception as e:
        app.logger.error("Error occurred while submitting: %s", str(e))
        return jsonify({"error": "An error occurred while submitting"}), 500


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(debug=False)