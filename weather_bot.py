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
    
    def test(self):
        msg = "Hello " + self.name
        self.sense.show_message(msg, scroll_speed=0.07)
        msg = "My city is " + self.city
        self.sense.show_message(msg, scroll_speed=0.07)
        
            