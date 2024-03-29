# !/usr/bin/env python3

# Standard Python libraries.
import datetime
import random

# Third-party Python libraries.
import TwitterSearch
from twython import Twython
from textblob import TextBlob


# Import API Keys for Auth
from auth import consumer_key, consumer_secret, access_token, access_token_secret

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


# Below is the script that will power the taco bot.

# This will use datetime to get the weekday.
# If it's Tuesday, it means Taco Tuesday.
def get_weekday():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayofweek = datetime.datetime.today().weekday()
    weekday = week[dayofweek]
    if weekday == "Tuesday":
        message = "It's Taco Tuesday!"
    else:
        message = f"It's {weekday}, meaning it's NOT Taco Tuesday."
        twitter.update_status(status=message)
        print(f"Tweeting {message}")
        return get_weekday


# Search for taco tweets and reply.
def search_tacos():
    ids_replied_to = []
    with open("./ids_replied_to.txt", "r") as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]
            # add item to the list
            ids_replied_to.append(current_place)

    # Search for the word "tacos."
    search_term = "tacos"
    print("Searching Twitter for 'tacos'...")
    results = twitter.cursor(twitter.search, q=search_term)

    for result in results:
        name = result["user"]
        screen_name = name["screen_name"]
        creation_date = result["created_at"]
        tweet_text = result["text"]
        id = result["id"]

        # Perform sentiment analyis using TextBlob
        # If sentiment is 0 or higher, tacobot will reply politely.
        getSentiment = TextBlob(tweet_text)
        getSentiment.sentiment
        getSentiment.sentiment.polarity
        print(getSentiment.sentiment.polarity)
        if getSentiment.sentiment.polarity >= 0:
            # post the tweet
            id = str(id)

            # Do not reply if tweet has already been replied to. This is to avoid spamming.
            if id in ids_replied_to:
                print("skipped as already replied to.")

            else:
                liketacos = open("./liketacos.txt").read().splitlines()
                likeTacos = random.choice(liketacos)
                twitter_handle = f"@{screen_name}"
                message = f"{twitter_handle} {likeTacos}"
                twitter.update_status(status=message, in_reply_to_status_id=id)
                print("Tweeted: %s" % message)
                id = int(id)
                ids_replied_to.append(id)
                with open("./ids_replied_to.txt", "w") as filehandle:
                    filehandle.writelines("%s\n" % place for place in ids_replied_to)
                break

        # If sentiment is below 0, tacobot will offer a rude reply.
        else:
            # post the tweet
            id = str(id)
            # Again, check if the tweet has already been replied to.
            if id in ids_replied_to:
                print("skipped as already replied to.")

            else:
                insults = open("./insults.txt").read().splitlines()
                theInsult = random.choice(insults)
                twitter_handle = f"@{screen_name}"
                message = f"{twitter_handle} {theInsult}"
                twitter.update_status(status=message, in_reply_to_status_id=id)
                print("Tweeted: %s" % message)
                id = int(id)
                ids_replied_to.append(id)
                with open("./ids_replied_to.txt", "w") as filehandle:
                    filehandle.writelines("%s\n" % place for place in ids_replied_to)
                break


# Fck da haterz!
# considering removing this now that we have sentiment analysis, but it's still kind of fun to have this codeblock.


def fk_tacos():
    ids_replied_to = []
    with open("./ids_replied_to.txt", "r") as filehandle:
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

        getSentiment = TextBlob(tweet_text)
        getSentiment.sentiment
        getSentiment.sentiment.polarity
        print(getSentiment.sentiment.polarity)
        if getSentiment.sentiment.polarity < 0:

            # post the tweet
            id = str(id)

            # Do not reply if tweet has already been replied to. This is to avoid spamming.
            if id in ids_replied_to:
                print("skipped as already replied to.")

            else:
                insults = open("./insults.txt").read().splitlines()
                theInsult = random.choice(insults)
                twitter_handle = f"@{screen_name}"
                message = f"{twitter_handle} {theInsult}"
                twitter.update_status(status=message, in_reply_to_status_id=id)
                print("Tweeted: %s" % message)
                id = int(id)
                ids_replied_to.append(id)
                with open("./ids_replied_to.txt", "w") as filehandle:
                    filehandle.writelines("%s\n" % place for place in ids_replied_to)
                break
        else:
            # post the tweet
            id = str(id)
            if id in ids_replied_to:
                print("skipped as already replied to.")

            else:
                liketacos = open("./liketacos.txt").read().splitlines()
                likeTacos = random.choice(liketacos)
                twitter_handle = f"@{screen_name}"
                message = f"{twitter_handle} {likeTacos}"
                twitter.update_status(status=message, in_reply_to_status_id=id)
                print("Tweeted: %s" % message)
                id = int(id)
                ids_replied_to.append(id)
                with open("./ids_replied_to.txt", "w") as filehandle:
                    filehandle.writelines("%s\n" % place for place in ids_replied_to)
                break


# Search for tweets about non-taco food, and reply suggesting tacos.
def search_non_tacos():
    ids_replied_to = []
    with open("./ids_replied_to.txt", "r") as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]
            # add item to the list
            ids_replied_to.append(current_place)

    search_terms = [
        "hamburger",
        "burger",
        "hotdog",
        "pizza",
        "sandwich",
        "burrito",
        "beef jerky",
        "bacon",
        "spaghetti",
        "eating tamales",
        "eating nachos",
        "steak",
    ]

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

        # Do not reply if tweet has already been replied to. This is to avoid spamming.
        if id in ids_replied_to:
            print("skipped as already replied to.")

        else:
            twitter_handle = f"@{screen_name}"
            message = (
                f"{twitter_handle} I mean, {randomFood} is cool, but have you considered tacos instead? Just an idea."
            )
            twitter.update_status(status=message, in_reply_to_status_id=id)
            print("Tweeted: %s" % message)
            id = int(id)
            ids_replied_to.append(id)
            with open("./ids_replied_to.txt", "w") as filehandle:
                filehandle.writelines("%s\n" % place for place in ids_replied_to)
            break


# This will get a random quote from a list of quotes and print it.
def get_random_quote():
    quotes = open("./tacoquotes.txt").read().splitlines()
    todaysQuote = random.choice(quotes)
    message = todaysQuote
    twitter.update_status(status=message)
    print(f"Tweeting {message}")
    return get_random_quote


# This will ask where to get tacos in a city pulled randomly from a list
# of cities and states.
def get_city_tacos():
    city_Tacos = open("./uscities.txt").read().splitlines()
    tacos_In_The_City = random.choice(city_Tacos)
    message = f"Does anyone know where I can get good tacos in {tacos_In_The_City}?"
    twitter.update_status(status=message)
    print(f"Tweeting {message}")
    return get_city_tacos


# This function is something of a "master" that will pull from a random list
# of functions that print taco things.
def tacobot_action():
    tacobot_actions = [get_weekday, get_random_quote, get_city_tacos, search_non_tacos, fk_tacos, search_tacos]
    random.choice(tacobot_actions)()
    quit()
    return tacobot_action


# This is really just for when I'm debugging or checking when Tacobot ran. Nothing really important here.
while True:
    gettheDate = datetime.datetime.now()
    rightNow = gettheDate.strftime("%x")
    print(f"Tacobot ran at {gettheDate}.")
    tacobot_action()


# To to:
# -- Figure out hattrick - Eating tacos for breakfast, lunch and dinner in
#    a single day will create hattrick.
