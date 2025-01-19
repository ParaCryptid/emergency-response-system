
import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Emergency Response System is fully functional.' in response.data

# Test adding an incident
def test_add_incident(client):
    data = {"description": "Fire in Sector 7", "priority": "High"}
    response = client.post('/add_incident', json=data)
    assert response.status_code == 200
    assert "Incident reported successfully." in response.get_json()["message"]

# Test retrieving incidents
def test_get_incidents(client):
    response = client.get('/get_incidents')
    assert response.status_code == 200
    incidents = response.get_json()
    assert isinstance(incidents, list)
    assert len(incidents) > 0

# Test adding a resource
def test_add_resource(client):
    data = {"name": "Fire Truck 3", "type": "Vehicle"}
    response = client.post('/add_resource', json=data)
    assert response.status_code == 200
    assert "Resource added successfully." in response.get_json()["message"]

# Test retrieving resources
def test_get_resources(client):
    response = client.get('/get_resources')
    assert response.status_code == 200
    resources = response.get_json()
    assert isinstance(resources, list)
    assert len(resources) > 0

# Test updating resource status
def test_update_resource_status(client):
    # Add a resource to update
    data = {"name": "Ambulance 1", "type": "Vehicle"}
    add_response = client.post('/add_resource', json=data)
    resource_id = add_response.get_json()["resource"]["id"]

    # Update the status
    update_data = {"id": resource_id, "status": "Deployed"}
    update_response = client.put('/update_resource_status', json=update_data)
    assert update_response.status_code == 200
    assert update_response.get_json()["resource"]["status"] == "Deployed"
