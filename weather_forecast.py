import requests

def forecast(MY_LAT, MY_LONG):
    """Takes arguments for latitude and longitude. Returns a dictionary titled forecast_data.
    forecast_data comprises Temp, Wind Speed, Wind Direction Forecast, Station, City, State, Weather Data"""

    # weather_response = requests.get(url="https://api.weather.gov")
    # weather_response = requests.get(url="https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast")

    # Collect the station ID, and grid coordinates for the coordinates from the national weather service
    weather_response_step_1 = requests.get(url=f"https://api.weather.gov/points/{MY_LAT},{MY_LONG}")
    weather_response_step_1.raise_for_status()
    station_data = weather_response_step_1.json()

    station = (station_data["properties"]["gridId"])
    gridx = (station_data["properties"]["gridX"])
    gridy = (station_data["properties"]["gridY"])
    city = (station_data["properties"]["relativeLocation"]["properties"]["city"])
    state = (station_data["properties"]["relativeLocation"]["properties"]["state"])


    # Next step - collect weather forecast from identified weather station and weather coordinates


    weather_response_step_2 = requests.get(url=f"https://api.weather.gov/gridpoints/{station}/{gridx},{gridy}/forecast")
    weather_response_step_2.raise_for_status()
    weather_data = weather_response_step_2.json()

    temperature = weather_data["properties"]["periods"][0]["temperature"]




    # for loop cycles through the json data to find the first hit for a "Tonight" forecast
    for n in range (0,5):
        if weather_data["properties"]["periods"][n]["name"] == "Tonight":
            tonights_forecast = n

    temperature = weather_data["properties"]["periods"][tonights_forecast]["temperature"]
    wind_speed = weather_data["properties"]["periods"][tonights_forecast]["windSpeed"]
    wind_direction = weather_data["properties"]["periods"][tonights_forecast]["windDirection"]
    forecast_details = weather_data["properties"]["periods"][tonights_forecast]["detailedForecast"]

    forecast_data = {"Temp":temperature, "Wind Speed": wind_speed, "Wind Direction": wind_direction,
                     "Forecast": forecast_details, "Station": station, "City": city, "State": state}

    return forecast_data
