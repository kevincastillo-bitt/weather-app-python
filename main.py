city = input("Enter city name: ").strip().lower()

weather_data = {
    "buenos aires": {"temp": 22, "condition": "Sunny"},
    "cordoba": {"temp": 18, "condition": "Cloudy"},
    "rosario": {"temp": 20, "condition": "Windy"},
    "mendoza": {"temp": 16, "condition": "Dry"},
    "la plata": {"temp": 21, "condition": "Partly cloudy"}
}

if city in weather_data:
    print(f"City: {city.title()}")
    print(f"Temperature: {weather_data[city]['temp']}°C")
    print(f"Condition: {weather_data[city]['condition']}")
else:
    print("City not found in local database.")
