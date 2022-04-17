import random

ye_lyrics = open("KW_VerseOnly.txt", "r")
ye_lyrics = ye_lyrics.readlines()

def get_random_lyric(data):
    lyrics = random.choice(data)
    lyrics = lyrics.split(",")
    for lyric in lyrics:
        lyric = lyrics[0]
    return lyric

ye_tweets = open("ye_tweets.csv",  "r")
ye_tweets = ye_tweets.readlines()

def get_random_tweet(data):
    tweets = random.choice(data[1:])
    tweets = tweets.split(",")
    for tweet in tweets:
        tweet = tweets[2]
    return tweet

def random_tweet_or_lyric():
    tweet = get_random_tweet(ye_tweets)
    lyric = get_random_lyric(ye_lyrics)
    response = random.choice([tweet, lyric])
    print(response)
    return response

random_tweet_or_lyric()
