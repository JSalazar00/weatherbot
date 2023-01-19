from sense_hat import SenseHat
from datetime import datetime
from keys import *
import time
from animations import * #Collaborated with Partner B
import requests

class WeatherBot:
    def __init__(self):
        self.sense = SenseHat()
        
        # Adding this to dim PI - it's too bright
        self.sense.low_light = True
        # self.key is the API Key needed to use the OpenWeatherMap API
        self.key = API_KEY
        
    def getuserinfo(self):
        """
        This function prompts the user for their name, city, state, country and
        the user's preferred temperature unit.
        
        """
        self.name = input("What is your name?: ")
        self.city = input("Enter a city: ")
        self.state = input("Enter State Code (i.e. TX): ")
        self.country = input("Enter Country Code (i.e. US or UK): ")
        self.tempUnit = input("Choose F or C: ").upper()
        
        if self.tempUnit == "F":
            self.unit  = "imperial"
        elif self.tempUnit == "C":
            self.unit = "metric"
    
    #TODO: if we use show_message, set scroll_speed to 0.07 
    def showcurrentWeather(self):
        """
        In this function, we will make a request to the OpenWeatherMap API
        to show the current weather. We will use the user's responses from the getuserinfo function.
        
        """
        # Greeting
        time.sleep(0.5)
        msg = "Hi, " + self.name
        self.sense.show_message(msg, scroll_speed=0.07)
        
        # Send request to OpenWeatherMap API
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + self.city + "," + self.state + "," + self.country + "&appid=" + self.key + "&units="+ self.unit
        response = requests.get(url).json()
        
        temp = str(int(response["main"]["temp"]))
        weather = response["weather"][0]["main"]
        dsc = response["weather"][0]["description"]
        
        # To do is to call animation function
        self.animation(weather)
        
        # Display temperature
        if self.tempUnit == "F":
            msg = "Temp is " + temp + "F"
        elif self.tempUnit == "C":
            msg = "Temp is " + temp + "C"
        self.sense.show_message(msg, scroll_speed=0.06)
        time.sleep(0.5)
        self.sense.show_message(dsc, scroll_speed=0.06)
        
        
    def animation(self, weather):
        """
        We are going show the proper animation based on the weather parameter.

        """
        if weather == "Clear":
            for x in range(0, 2):
                self.sense.set_pixels(clear_skies)
                time.sleep(0.5)
                self.sense.set_pixels(clear_skies2)
                time.sleep(0.5)
                self.sense.set_pixels(clear_skies3)
                time.sleep(0.5)
                self.sense.set_pixels(clear_skies4)
                time.sleep(0.5)
        elif weather == "Clouds":
            for x in range(0, 2):
                self.sense.set_pixels(cloud)
                time.sleep(0.5)
                self.sense.set_pixels(cloud2)
                time.sleep(0.5)
                self.sense.set_pixels(cloud3)
                time.sleep(0.5)
        elif weather == "Rain":
            for x in range(0, 2):
                self.sense.set_pixels(rain)
                time.sleep(0.5)
                self.sense.set_pixels(rain2)
                time.sleep(0.5)
        elif weather == "Blizzard":
            for x in range(0, 2):
                self.sense.set_pixels(blizzard)
                time.sleep(0.5)
                self.sense.set_pixels(blizzard2)
                time.sleep(0.5)
                self.sense.set_pixels(blizzard3)
                time.sleep(0.5)
        elif weather == "Mist":
            for x in range(0,2):
                self.sense.set_pixels(mist1)
                time.sleep(0.5)
                self.sense.set_pixels(mist2)
                time.sleep(0.5)
        
                
                
                
            
            
                
         
        
        
        
        
        
            