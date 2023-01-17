from sense_hat import SenseHat
import time

sense = SenseHat()

name = input("enter name:")

age = input("enter your age:")

msg = "Your name is " + name
sense.show_message(msg)

time.sleep(1)
msg = "You are " + age + " years old"
sense.show_message(msg)