from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/',methods=['GET'])

def home():
    return jsonify({"message": "Weather App is Running!", "status": "healthy"})

@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "OK", "version": "1.0"}),200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    
