import os
import random
import datetime
import json

def generate_sensor_data():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "radiation": round(random.uniform(0.01, 0.25), 3),
        "biohazard_level": random.randint(0, 5),
        "chemical_ppm": round(random.uniform(10.0, 300.0), 1),
        "temperature_C": round(random.uniform(15.0, 45.0), 1),
        "humidity_percent": random.randint(20, 80),
        "sensor_mode": "simulated"
    }

def save_sensor_data(data, output_folder="../classified"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(output_folder, f"sensor_sim_{timestamp}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[✓] Simulated sensor data written: {path}")

if __name__ == "__main__":
    print("[*] Running Sensor Simulation Module...")
    os.makedirs("../classified", exist_ok=True)
    data = generate_sensor_data()
    save_sensor_data(data)
