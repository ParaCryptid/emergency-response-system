
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import random
import geojson
from transformers import pipeline

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize AI models (e.g., sentiment analysis for emergencies)
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return jsonify({
        "message": "Emergency Response System repository is fully functional.",
        "features": [
            "AI-Enhanced Alerts",
            "Real-Time Geospatial Monitoring",
            "Secure Collaboration"
        ]
    })

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json.get("text", "")
    if not data:
        return jsonify({"error": "No text provided"}), 400
    analysis = sentiment_analyzer(data)
    return jsonify({"analysis": analysis})

@app.route('/geospatial_event', methods=['POST'])
def report_geospatial_event():
    data = request.json
    if not data or "latitude" not in data or "longitude" not in data:
        return jsonify({"error": "Invalid geospatial data"}), 400

    event = geojson.Feature(
        geometry=geojson.Point((data["longitude"], data["latitude"])),
        properties={"event_type": data.get("event_type", "Unknown")}
    )
    # Simulate broadcasting the event in real-time
    socketio.emit("geospatial_event", {"event": geojson.dumps(event)})
    return jsonify({"message": "Geospatial event reported successfully", "event": event})

@socketio.on('connect')
def handle_connect():
    emit("message", {"message": "Real-time alerts connection established"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
