import requests
import datetime


def twilight(latitude, longitude, tomorrow):
    """Inputs: latitude, longitude, and tomorrow's date in YYYY-MM-DD format.
    Returns the nautical twilight beginning and end, and the astronomical twilight
    beginning and end in a dictionary celestial_data. celestial_data contains
    AstronomicalTwilightNight, AstronomicalTwilightDay, NauticalTwilightNight,
    NauticalTwilightDay"""

   # -------------Parameters------------------------------
    # parameters formatted per the API's requested inputs found here:
    # https://sunrise-sunset.org/api

    # formatted parameters are used to collect a formatted response from the API to be used in the GUI
    # unformatted parameters are used to compare time against the ISS being overhead.

    # Nightfall parameters

    parameters_unformatted_nightfall = {
        "lat": latitude,
        "long": longitude,
        "formatted": 0
    }

    parameters_formatted_nightfall = {
        "lat": latitude,
        "long": longitude,
        "formatted": 1

    }

    # Daybreak parameters
    parameters_unformatted_daybreak = {
        "lat": latitude,
        "long": longitude,
        "formatted": 0,
        "date": tomorrow
    }

    parameters_formatted_daybreak = {
        "lat": latitude,
        "long": longitude,
        "formatted": 1,
        "data": tomorrow

    }

    # Unformatted data - nightfall

    gps_response_unform_nightfall = requests.get(url="https://api.sunrise-sunset.org/json",
                                                 params=parameters_unformatted_nightfall)
    gps_response_unform_nightfall.raise_for_status
    gps_data_unform_nightfall = gps_response_unform_nightfall.json()

    nautical_twilight_night_hr = gps_data_unform_nightfall["results"]["nautical_twilight_end"].split("T")[1].split(":")[
        0]
    nautical_twilight_night_min = \
    gps_data_unform_nightfall["results"]["nautical_twilight_end"].split("T")[1].split(":")[1]

    astronomical_twilight_night_hr = \
    gps_data_unform_nightfall["results"]["astronomical_twilight_end"].split("T")[1].split(":")[0]
    astronomical_twilight_night_min = \
    gps_data_unform_nightfall["results"]["astronomical_twilight_end"].split("T")[1].split(":")[1]



    # formated data for user interface - nightfall
    gps_response_form_nightfall = requests.get(url="https://api.sunrise-sunset.org/json",
                                               params=parameters_formatted_nightfall)
    gps_response_form_nightfall.raise_for_status
    gps_data_form_nightfall = gps_response_form_nightfall.json()
    # print(f"Debugging line... {gps_data_form_nightfall}")
    nautical_twilight_night = gps_data_form_nightfall["results"]["nautical_twilight_end"]

    astronomical_twilight_night = gps_data_form_nightfall["results"]["astronomical_twilight_end"]



    # Unformatted date - daybreak
    gps_response_unform_daybreak = requests.get(url="https://api.sunrise-sunset.org/json",
                                                params=parameters_unformatted_daybreak)
    gps_response_unform_daybreak.raise_for_status
    gps_data_unform_daybreak = gps_response_unform_daybreak.json()

    naughtical_twilight_day_hr = \
    gps_data_unform_daybreak["results"]["nautical_twilight_begin"].split("T")[1].split(":")[0]
    naughtical_twilight_day_min = \
    gps_data_unform_daybreak["results"]["nautical_twilight_begin"].split("T")[1].split(":")[1]

    astronomical_twilight_day_hr = \
    gps_data_unform_daybreak["results"]["astronomical_twilight_begin"].split("T")[1].split(":")[0]
    astronomical_twilight_day_min = \
    gps_data_unform_daybreak["results"]["astronomical_twilight_begin"].split("T")[1].split(":")[1]


    # formatted daybreak


    gps_response_form_daybreak = requests.get(url="https://api.sunrise-sunset.org/json",
                                              params=parameters_formatted_daybreak)
    gps_response_form_daybreak.raise_for_status

    gps_data_form_daybreak = gps_response_form_daybreak.json()

    nautical_twilight_day = gps_data_form_daybreak["results"]["nautical_twilight_begin"]

    astronomical_twilight_day = gps_data_form_daybreak["results"]["astronomical_twilight_begin"]

    celestial_data = {"NauticalTwilightNight": nautical_twilight_night, "NauticalTwilightMorning": nautical_twilight_day,
                      "AstronomicalTwilightNight": astronomical_twilight_night,
                      "AstronomicalTwilightMorning": astronomical_twilight_day}
    return celestial_data
