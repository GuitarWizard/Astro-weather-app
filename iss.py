import requests

def international_space_station_gps():
    """Requests the current coordinates of the international space station. Returns
    (latitude, longitude)
    The API is found here:
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/"""

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_gps = iss_response.json()

    longitude = float(iss_gps["iss_position"]["longitude"])
    latitude = float(iss_gps["iss_position"]["latitude"])
    iss_position = (latitude, longitude)
    return iss_position
