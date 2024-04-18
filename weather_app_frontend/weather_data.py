import datetime

weather_forecast = [
    {
        "status": 0,
        "error": "",
        "day": {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.datetime(2024, 4, 10, 17, 18).strftime(
                "%a %m %b %Y %H:%M:%S"
            ),
            "weather": {"description": "Sunny", "icon": "☀️"},
            "temperature": {"real": 16, "feel": 16, "humidity": "42 %"},
            "wind": {"speed": 9},
        },
        "week": None,
    },
    {
        "status": 0,
        "error": "",
        "day": {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.datetime(2024, 4, 10, 17, 18).strftime(
                "%a %m %b %Y %H:%M:%S"
            ),
            "weather": {"description": "Sunny", "icon": "☀️"},
            "temperature": {"real": 16, "feel": 16, "humidity": "42 %"},
            "wind": {"speed": 9},
        },
        "week": None,
    },
    {
        "status": 0,
        "error": "",
        "day": {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.datetime(2024, 4, 10, 17, 18).strftime(
                "%a %m %b %Y %H:%M:%S"
            ),
            "weather": {"description": "Sunny", "icon": "☀️"},
            "temperature": {"real": 16, "feel": 16, "humidity": "42 %"},
            "wind": {"speed": 9},
        },
        "week": None,
    },
    {
        "status": 0,
        "error": "",
        "day": {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.datetime(2024, 4, 10, 17, 18).strftime(
                "%a %m %b %Y %H:%M:%S"
            ),
            "weather": {"description": "Sunny", "icon": "☀️"},
            "temperature": {"real": 16, "feel": 16, "humidity": "42 %"},
            "wind": {"speed": 9},
        },
        "week": None,
    },
]

print(weather_forecast)


weather_forecast_2 = {
    "status": 0,
    "error": "",
    "day": {
        "location": {
            "name": "Paris",
            "region": "Ile-de-France",
            "country": "France",
            "latitude": 48.86,
            "longitude": 2.35,
        },
        "date": datetime.datetime(2024, 4, 11, 9, 50).strftime(
            "%a %m %b %Y %H:%M:%S"
        ),
        "weather": {"description": "Partly cloudy", "icon": "⛅️"},
        "temperature": {"real": 14, "feel": 13, "humidity": 77},
        "wind": {"speed": 11},
    },
    "week": [
        {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.date(2024, 4, 11).strftime("%a %m %b"),
            "temperature": {"high": 16, "low": 11, "average": 13},
            "ephemeride": {
                "sun": {
                    "rise": datetime.time(7, 7).strftime("%H:%M"),
                    "light": 9.8,
                    "set": datetime.time(20, 37).strftime("%H:%M"),
                },
                "moon": {
                    "rise": datetime.time(8, 9).strftime("%H:%M"),
                    "phase": "🌒",
                    "set": None,
                    "light": 7,
                },
            },
        },
        {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.date(2024, 4, 12).strftime("%a %m %b"),
            "temperature": {"high": 22, "low": 13, "average": 17},
            "ephemeride": {
                "sun": {
                    "rise": datetime.time(7, 5).strftime("%H:%M"),
                    "light": 12.8,
                    "set": datetime.time(20, 38).strftime("%H:%M"),
                },
                "moon": {
                    "rise": datetime.time(8, 42).strftime("%H:%M"),
                    "phase": "🌒",
                    "set": datetime.time(0, 50).strftime("%H:%M"),
                    "light": 14,
                },
            },
        },
        {
            "location": {
                "name": "Paris",
                "region": "Ile-de-France",
                "country": "France",
                "latitude": 48.86,
                "longitude": 2.35,
            },
            "date": datetime.date(2024, 4, 13).strftime("%a %m %b"),
            "temperature": {"high": 24, "low": 13, "average": 18},
            "ephemeride": {
                "sun": {
                    "rise": datetime.time(7, 3).strftime("%H:%M"),
                    "light": 12.3,
                    "set": datetime.time(20, 40).strftime("%H:%M"),
                },
                "moon": {
                    "rise": datetime.time(9, 27).strftime("%H:%M"),
                    "phase": "🌒",
                    "set": datetime.time(2, 7).strftime("%H:%M"),
                    "light": 23,
                },
            },
        },
    ],
}


# list of data for the evolution of the week
temperatures_chart = [
    {
        "name": weather_forecast_2["week"][0]["date"],
        "high": weather_forecast_2["week"][0]["temperature"]["high"],
        "average": weather_forecast_2["week"][0]["temperature"]["average"],
        "low": weather_forecast_2["week"][0]["temperature"]["low"],
    },
    {
        "name": weather_forecast_2["week"][1]["date"],
        "high": weather_forecast_2["week"][1]["temperature"]["high"],
        "average": weather_forecast_2["week"][1]["temperature"]["average"],
        "low": weather_forecast_2["week"][1]["temperature"]["low"],
    },
    {
        "name": weather_forecast_2["week"][2]["date"],
        "high": weather_forecast_2["week"][2]["temperature"]["high"],
        "average": weather_forecast_2["week"][2]["temperature"]["average"],
        "low": weather_forecast_2["week"][2]["temperature"]["low"],
    },
]


print(temperatures_chart)
