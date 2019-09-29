# !/usr/bin/env python3

# Standard Python libraries.
import datetime
import json
import time
import random
import sys


# Third-party Python libraries.
import requests
import TwitterSearch
from twython import Twython

# Custom Python libraries.
# Import API Keys for Auth
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

twitter = Twython(consumer_key, consumer_secret, access_token,access_token_secret)



# Below is the script that will power the taco bot.

# This will use datetime to get the weekday.
# If it's Tuesday, it means Taco Tuesday.

def getweekday():
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dayofweek = datetime.datetime.today().weekday()
    weekday = (week[dayofweek])
    if weekday == "Tuesday":
        print("It's Taco Tuesday!")
    else:
        print(f"It's {weekday}, meaning it's NOT Taco Tuesday.")
    return getweekday


# This will get a random quote from a list of quotes and print it.
def getRandomQuote():
    quotes = open('tacoquotes.txt').read().splitlines()
    todaysQuote = random.choice(quotes)
    print(todaysQuote)
    return getRandomQuote


# This will ask where to get tacos in a city pulled randomly from a list
# of cities and states.
def getCityTacos():
    cityTacos = open('uscities.txt').read().splitlines()
    tacosinthecity = random.choice(cityTacos)
    #print(f"Does anyone know where I can get good tacos in {tacosinthecity}?")
    return getCityTacos

"""
def searchTacos():
    print("I see you're talking about tacos. I like tacos.")
    This is still in the works. It will search twitter for taco tweets and
    it will reply to the tweet with "I see you're talking about tacos."
"""


# This function is something of a "master" that will pull from a random list
# of functions that print taco things.


def tacobotAction():
    tacobotActions = [getweekday, getRandomQuote, getCityTacos]
    random.choice(tacobotActions)()
    # Set tweeting times to long, random intervals
    #whenToTweet = [10800, 3600, 7200, 21600, 16200, 8640, 18360] # Random interval for tweets.
    whenToTweet = [9,5]
    whenToTweet = random.choice(whenToTweet)
    time.sleep(whenToTweet) # Pause for a random number of seconds (hours) then tweet again.







"""

    #twitter.update_status(status=)

"""






#tacobotAction()
#twitter.update_status(status=)

# To to:
# -- Figure out hattrick - Eating tacos for breakfast, lunch and dinner in
#    a single day will create hattrick.
# -- Search taco tweets. Will reply "Hey. I see you're talking about tacos."
