import geojson

def create_geo_event(latitude, longitude, event_type="Unknown"):
    return geojson.Feature(
        geometry=geojson.Point((longitude, latitude)),
        properties={"event_type": event_type}
    )
