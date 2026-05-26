import os
import requests
from flask import Flask, jsonify
app = Flask(__name__)

#get api url from environment 
API_URL  = os.getenv('API_URL', 'http://localhost:5001')

@app.route('/',methods=['GET'])

def home():
    return jsonify({"message": "Weather App is Running!", "status": "healthy"})

@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "OK", "version": "1.0"}),200

@app.route('/fetch-weather',methods=['GET'])
def fetch_weather():
    """Fetch weather from API service"""
    try:
        city = 'Delhi'  # Default city
        response = requests.get(f"{API_URL}/api/weather?city={city}")
        data = response.json()
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

