# Weather App

A simple console application that displays weather information for a given city. Built as a portfolio project to practice clean code and modular design in Python.

## Features

- Search weather by city name
- Display temperature, condition, humidity, and wind speed
- Input validation and error handling
- Loop to check multiple cities
- Clean formatted output

## Project Structure

weather-app-python/
├── main.py
├── requirements.txt
└── README.md

## Code Organization

The code is organized into five functions, each with a single responsibility:

| Function | Purpose |
|----------|---------|
| `get_city()` | Ask user for city name and validate input |
| `get_weather()` | Retrieve weather data from local database |
| `display_weather()` | Show formatted weather information |
| `ask_continue()` | Check if user wants another search |
| `main()` | Coordinate the program flow |

The data is stored in a dictionary, making it easy to replace with a real API later.

## How to Run

```bash
python main.py
```

## Example

```
=============================================
  🌦️  WELCOME TO THE WEATHER APP
=============================================

📋 Available cities: Bariloche, Buenos Aires, Córdoba, Mendoza, Rosario

🌍 Enter a city name: buenos aires

=============================================
  🌤️  WEATHER REPORT: Buenos Aires
=============================================
  ☀️ Condition:   Sunny
  🌡️  Temperature:  24°C
  💧 Humidity:    65%
  💨 Wind:        12 km/h
=============================================

🔍 Check another city? (y/n): n

=============================================
  👋 Thank you for using the Weather App!
=============================================
```

## Requirements

Python 3.7 or higher  
No external dependencies required

## Author

Kevin Castillo  
GitHub: @kevincastillo-bitt
