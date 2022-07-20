import requests
import json
import datetime
from twilight import *
from iss import *
from weather_forecast import *


# -----------My current location------------------------

MY_LAT = 30.955991
MY_LONG = -120.642752
# ----------Current date and tomorrow ------------------
date = datetime.datetime.now()


date_tomorrow = (date + datetime.timedelta(days=1))
date_tomorrow = (f"{date_tomorrow.year}-{date_tomorrow.month}-{date_tomorrow.day}")

# -----------------ISS location---------------------------------------------------
iss_location = international_space_station_gps()


# ----------Celestials----------------------------
celestial_data = twilight(latitude= MY_LAT, longitude= MY_LONG, tomorrow=date_tomorrow)

# ------------Weather Forecasting------------------------------------------
forecast_data = forecast(MY_LAT, MY_LONG)

print("\nWeather data---------------\n")

temperature = forecast_data["Temp"]
wind = (forecast_data["Wind Speed"], forecast_data["Wind Direction"])
local_weather = forecast_data["Forecast"]
weather_station = forecast_data["Station"]
city = forecast_data["City"]
state = forecast_data["State"]

nautical_twilight_night = celestial_data["NauticalTwilightNight"]
astronomical_twilight_night = celestial_data["AstronomicalTwilightNight"]
astronomical_twilight_day = celestial_data["AstronomicalTwilightMorning"]
nautical_twilight_day = celestial_data["NauticalTwilightMorning"]
print("Weather Data:")
print(temperature, wind, local_weather, weather_station, city, state)
print('\n')
print("Sunset Data:")
print(f"Nautical Twilight: {nautical_twilight_night}")
print(f"Astronimical Twilight: {astronomical_twilight_night}")
print(f"Nautical Twilight Morning: {nautical_twilight_day}")

if abs(iss_location[0]-MY_LAT) <= 5 and abs(iss_location[1]-MY_LONG) <=5:
    print("The I.S.S. is overhead!")
print(f"I.S.S. Location: {iss_location}")
# temperature_unit = weather_data["properties"]["periods"]["temperatureUnit"]
# print(temperature_unit)

