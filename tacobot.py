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
from auth import consumer_key, consumer_secret, access_token, access_token_secret

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# Below is the script that will power the taco bot.

# This will use datetime to get the weekday.
# If it's Tuesday, it means Taco Tuesday.
def getweekday():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayofweek = datetime.datetime.today().weekday()
    weekday = week[dayofweek]
    if weekday == "Tuesday":
        message = "It's Taco Tuesday!"
    else:
        message = f"It's {weekday}, meaning it's NOT Taco Tuesday."
        twitter.update_status(status=message)
        print(f"Tweeting {message}")
        return getweekday


####################################
# Search for taco tweets and reply.#
####################################


def searchTacos():
    ids_replied_to = []
    with open("ids_replied_to.txt", "r") as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]
            # add item to the list
            ids_replied_to.append(current_place)

    search_term = "tacos"
    print("Searching Twitter for 'tacos'...")
    results = twitter.cursor(twitter.search, q=search_term)

    for result in results:
        name = result["user"]
        screen_name = name["screen_name"]
        creation_date = result["created_at"]
        tweet_text = result["text"]
        id = result["id"]

        # post the tweet
        id = str(id)
        if id in ids_replied_to:
            print("skipped as already replied to.")
            print()
            print()
        else:
            twitter_handle = f"@{screen_name}"
            message = f"{twitter_handle} Hey! I see you're talking about tacos. I like tacos!"
            twitter.update_status(status=message, in_reply_to_status_id=id)
            print("Tweeted: %s" % message)
            id = int(id)
            ids_replied_to.append(id)
            with open("ids_replied_to.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % place for place in ids_replied_to)
            break


#######################
#    Fck da haterz   #
######################


def fkTacos():
    ids_replied_to = []
    with open("ids_replied_to.txt", "r") as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]
            # add item to the list
            ids_replied_to.append(current_place)

    search_term = "fuck tacos"
    print("Searching Twitter for 'fuck tacos'...")
    results = twitter.cursor(twitter.search, q=search_term)

    for result in results:
        name = result["user"]
        screen_name = name["screen_name"]
        creation_date = result["created_at"]
        tweet_text = result["text"]
        id = result["id"]

        # post the tweet
        id = str(id)
        if id in ids_replied_to:
            print("skipped as already replied to.")
            print()
            print()
        else:
            insults = open("insults.txt").read().splitlines()
            theInsult = random.choice(insults)
            twitter_handle = f"@{screen_name}"
            message = f"{twitter_handle} {theInsult}"
            twitter.update_status(status=message, in_reply_to_status_id=id)
            print("Tweeted: %s" % message)
            id = int(id)
            ids_replied_to.append(id)
            with open("ids_replied_to.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % place for place in ids_replied_to)
            break


######################################
# Search for taco tweets and reply.  #
#####################################


def searchNonTacos():
    ids_replied_to = []
    with open("ids_replied_to.txt", "r") as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]
            # add item to the list
            ids_replied_to.append(current_place)

    search_terms = ["hamburger", "burger", "hotdog", "pizza", "sandwich"]
    randomFood = random.choice(search_terms)
    print(f"Searching Twitter for {randomFood} ...")
    results = twitter.cursor(twitter.search, q=randomFood)

    for result in results:
        name = result["user"]
        screen_name = name["screen_name"]
        creation_date = result["created_at"]
        tweet_text = result["text"]
        id = result["id"]

        # post the tweet
        id = str(id)
        if id in ids_replied_to:
            print("skipped as already replied to.")
            print()
            print()
        else:
            twitter_handle = f"@{screen_name}"
            message = (
                f"{twitter_handle} I mean, {randomFood} is cool, but have you considered tacos instead? Just an idea."
            )
            twitter.update_status(status=message, in_reply_to_status_id=id)
            print("Tweeted: %s" % message)
            id = int(id)
            ids_replied_to.append(id)
            with open("ids_replied_to.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % place for place in ids_replied_to)
            break


# This will get a random quote from a list of quotes and print it.
def getRandomQuote():
    quotes = open("tacoquotes.txt").read().splitlines()
    todaysQuote = random.choice(quotes)
    message = todaysQuote
    twitter.update_status(status=message)
    print(f"Tweeting {message}")
    return getRandomQuote



# This will ask where to get tacos in a city pulled randomly from a list
# of cities and states.
def getCityTacos():
    cityTacos = open("uscities.txt").read().splitlines()
    tacosinthecity = random.choice(cityTacos)
    message = f"Does anyone know where I can get good tacos in {tacosinthecity}?"
    twitter.update_status(status=message)
    print(f"Tweeting {message}")
    return getCityTacos


# This function is something of a "master" that will pull from a random list
# of functions that print taco things.


def tacobotAction():
    tacobotActions = [getweekday, getRandomQuote, getCityTacos, searchNonTacos, fkTacos, searchTacos]
    random.choice(tacobotActions)()
    # Set tweeting times to long, random intervals
    #whenToTweet = [3600, 7200, 10800, 18000, 7380, 14400, 18600, 5400, 21600]  # Random interval for tweets.
    #whenToTweet = random.choice(whenToTweet)
    #print(f" TacoBot will pause for {whenToTweet} seconds before tweeting again.")
    #time.sleep(whenToTweet)  # Pause for a random number of seconds (hours) then tweet again.
    quit()
    return tacobotAction



while True:
    gettheDate = datetime.datetime.now()
    rightNow = gettheDate.strftime("%x")
    print(f"Tacobot ran at {gettheDate}.")
    tacobotAction()


# To to:
# -- Figure out hattrick - Eating tacos for breakfast, lunch and dinner in
#    a single day will create hattrick.





























