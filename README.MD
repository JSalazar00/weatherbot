# Weather Bot
## Overview
The Weather Bot is designed to tell the user the weather from a given location. The output is displayed on a Raspberry Pi Sense HAT by showing the temperature, weather animation, and description.

## How It Works
1.) Prompts the user for their name, city, state code, country code, and temperature unit.
2.) Code obtains data from the OpenWeather API using info from the user by sending a request to their server
3.) Code receives response from API in the form of JavaScript Object Notation (JSON). Here is an example of what that looks like

### Data
```
{
  "coord": {
    "lon": -95.6972,
    "lat": 29.9691
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 46.35,
    "feels_like": 43.47,
    "temp_min": 44.4,
    "temp_max": 48.72,
    "pressure": 1011,
    "humidity": 92
  },
  "visibility": 10000,
  "wind": {
    "speed": 5.75,
    "deg": 290
  },
  "clouds": {
    "all": 0
  },
  "dt": 1674614007,
  "sys": {
    "type": 2,
    "id": 2001607,
    "country": "US",
    "sunrise": 1674566215,
    "sunset": 1674604347
  },
  "timezone": -21600,
  "id": 4684724,
  "name": "Cypress",
  "cod": 200
}
```

4.) Output
  * Greets user
  * Show animation based on Data["weather"][0]["main"]
  * Show temperature Data["main"]["temp"]
  * Show weather description Data["weather"][0]["description"]

## Instructions
### What's needed
* Raspberry Pi that is compatible with Sense HAT
* Sense HAT
* API Key from OpenWeatherMap API

1.) Install the libraries
```
sudo apt-get update
sudo apt-get install sense-hat 
```

```
pip3 install requests
```

2.) Create a file called keys.py
```
API_KEY=<your key>
```

3.) Ensure you have the following files:
    * main.py
    * animataions.py
    * weather_bot.py
    * keys.py

4.) Run the main file
```
python3 main.py
```

## Special Thanks
* [OpenWeatherMap API](https://openweathermap.org/), for allowing me to use their server
* [Raspberry Pi Sense HAT](https://www.raspberrypi.com/documentation/accessories/sense-hat.html), for showing the output of the code in a creative way
* [Requests](https://pypi.org/project/requests/), made sending requests easy
* My mentor for collaborating with me on this project and teaching me how to achieve my goals with this project.
    
    