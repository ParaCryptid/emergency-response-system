
# Emergency Response System

## Overview
The Emergency Response System has been enhanced with new features to improve functionality and security.

### New Features
1. **AI-Enhanced Alerts**
    - Endpoint: `/analyze`
    - Method: `POST`
    - Description: Analyzes provided text for sentiment to prioritize emergencies.
    - Example Request:
      ```json
      {
          "text": "Emergency at location X, situation critical."
      }
      ```
    - Example Response:
      ```json
      {
          "analysis": [{"label": "NEGATIVE", "score": 0.99}]
      }
      ```

2. **Real-Time Geospatial Monitoring**
    - Endpoint: `/geospatial_event`
    - Method: `POST`
    - Description: Reports geospatial events and broadcasts them in real-time.
    - Example Request:
      ```json
      {
          "latitude": 34.05,
          "longitude": -118.25,
          "event_type": "Fire"
      }
      ```
    - Example Response:
      ```json
      {
          "message": "Geospatial event reported successfully",
          "event": {...}
      }
      ```

### Real-Time Alerts
The system uses Flask-SocketIO to provide real-time updates for geospatial events and other emergencies.

## Getting Started
1. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python app.py
    ```
