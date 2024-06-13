from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'pootharekulu',
    'password': 'N!hal4444',
    'database': 'pootharekulu'
}

# Define your API routes
@app.route('/api/offers')
def get_offers():
    try:
        # Create MySQL connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM offers")

        # Fetch data
        offers = cursor.fetchall()

        # Close connection
        cursor.close()
        conn.close()

        # Convert data to JSON format and return
        return jsonify(offers)
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

