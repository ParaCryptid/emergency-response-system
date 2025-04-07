from flask import jsonify, request
from services.ai import analyze_sentiment
from services.geo import create_geo_event
import geojson

def api_routes(app):
    @app.route("/")
    def home():
        return jsonify({
            "message": "Emergency Response System repository is fully functional.",
            "features": [
                "AI-Enhanced Alerts",
                "Real-Time Geospatial Monitoring",
                "Secure Collaboration"
            ]
        })

    @app.route("/analyze", methods=["POST"])
    def analyze_text():
        data = request.json.get("text", "")
        if not data:
            return jsonify({"error": "No text provided"}), 400
        analysis = analyze_sentiment(data)
        return jsonify({"analysis": analysis})

    @app.route("/geospatial_event", methods=["POST"])
    def report_geospatial_event():
        data = request.json
        if not data or "latitude" not in data or "longitude" not in data:
            return jsonify({"error": "Invalid geospatial data"}), 400

        event = create_geo_event(data["latitude"], data["longitude"], data.get("event_type", "Unknown"))
        from flask_socketio import emit
        emit("geospatial_event", {"event": geojson.dumps(event)}, broadcast=True)
        return jsonify({"message": "Geospatial event reported successfully", "event": geojson.dumps(event)})
