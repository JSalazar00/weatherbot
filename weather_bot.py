from sense_hat import SenseHat
from datetime import datetime
import time
from animations import * #Collaborated with Partner B
import requests

class WeatherBot:
    def __init__(self):
        self.sense = SenseHat()
        
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
        
            