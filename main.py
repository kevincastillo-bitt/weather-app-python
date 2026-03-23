"""
WEATHER APP
-----------
A simple console application that displays weather information for a given city.
Uses a local database (dictionary) as the data source.
"""

# ==================== DATA ====================

WEATHER_DATA = {
    "buenos aires": {
        "temperature": 24,
        "condition": "Sunny",
        "humidity": 65,
        "wind": 12
    },
    "cordoba": {
        "temperature": 22,
        "condition": "Partly Cloudy",
        "humidity": 70,
        "wind": 10
    },
    "rosario": {
        "temperature": 23,
        "condition": "Cloudy",
        "humidity": 75,
        "wind": 8
    },
    "mendoza": {
        "temperature": 28,
        "condition": "Sunny",
        "humidity": 45,
        "wind": 15
    },
    "bariloche": {
        "temperature": 12,
        "condition": "Rainy",
        "humidity": 85,
        "wind": 20
    }
}


# ==================== FUNCTIONS ====================

def get_city():
    while True:
        city = input("\nEnter a city name: ").strip()
        
        if not city:
            print("Error: Please enter a city name.\n")
            continue
        
        city_lower = city.lower()
        
        if city_lower in WEATHER_DATA:
            return city_lower
        
        print(f"Sorry, '{city}' is not in our database.")
        print("Available cities: Buenos Aires, Cordoba, Rosario, Mendoza, Bariloche\n")


def get_weather(city):
    return WEATHER_DATA.get(city, {})


def display_weather(city, data):
    print("\n" + "=" * 40)
    print(f"WEATHER REPORT: {city.title()}")
    print("=" * 40)
    print(f"Condition: {data['condition']}")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind: {data['wind']} km/h")
    print("=" * 40)


def ask_continue():
    while True:
        choice = input("\nCheck another city? (y/n): ").strip().lower()
        
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")


def main():
    print("=" * 40)
    print("WELCOME TO THE WEATHER APP")
    print("=" * 40)

    while True:
        city = get_city()
        weather = get_weather(city)
        display_weather(city, weather)

        if not ask_continue():
            break

    print("\nThanks for using the Weather App!")


if __name__ == "__main__":
    main()
