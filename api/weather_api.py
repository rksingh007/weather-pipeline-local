from flask import Flask, jsonify, request

api = Flask(__name__)

# Mock weather data
MOCK_DATA = {
    "Delhi": {"temp": 35, "humidity": 60, "condition": "Sunny"},
    "Mumbai": {"temp": 30, "humidity": 75, "condition": "Rainy"},
    "Bangalore": {"temp": 28, "humidity": 65, "condition": "Cloudy"}
}

@api.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Delhi')
    if city in MOCK_DATA:
        return jsonify({"city": city, "data": MOCK_DATA[city]}), 200
    return jsonify({"error": "City not found"}), 404

@api.route('/api/health', methods=['GET'])
def api_health():
    return jsonify({"service": "weather-api", "status": "healthy"}), 200

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5001, debug=True)