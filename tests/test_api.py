import unittest
from main import app
from services.ai import analyze_sentiment
from services.geo import create_geo_event
import os

class EmergencyResponseTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Emergency Response System", response.get_json()["message"])

    def test_analyze_text_valid(self):
        response = self.app.post('/analyze', json={"text": "Emergency alert"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.get_json())

    def test_analyze_text_invalid(self):
        response = self.app.post('/analyze', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_geospatial_event_valid(self):
        payload = {"latitude": 34.05, "longitude": -118.25, "event_type": "Fire"}
        response = self.app.post('/geospatial_event', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    def test_geospatial_event_invalid(self):
        response = self.app.post('/geospatial_event', json={"lat": 0})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_ai_service(self):
        result = analyze_sentiment("This is urgent")
        self.assertTrue(isinstance(result, list))
        self.assertIn("label", result[0])

    def test_geo_service(self):
        geo = create_geo_event(10.0, 20.0, "Test")
        self.assertIn("geometry", geo)

if __name__ == '__main__':
    unittest.main()
