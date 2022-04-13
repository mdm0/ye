import random

ye_twitter = open("ye_tweets.csv", "r")
read_tweets = ye_twitter.readlines()

def get_random_tweet():
    random_tweets = random.choice(read_tweets[1:])
    random_tweets = random_tweets.split(",")
    
    for tweet in random_tweets:
        tweet = random_tweets[2]
        time = str(random_tweets[1])
        date = str(random_tweets[0])

        year = date[2:4] + " "
        month = date[4:6] + "/"
        day = date[6:] + "/"
        time = time[:2] + ":" + time[2:]
        full_date = month + day + year + time
        
        # tweet = tweet + "\n"  +  full_date + "\n"
        
    return tweet

YeLyrics = open("Ye Lyrics.csv", "r")
ReadLyrics = YeLyrics.readlines()

def YeRandomLyrics():
    RandomLyrics = random.choice(ReadLyrics[1:])
    RandomLyrics = RandomLyrics.split(",")
    
    for lyric in RandomLyrics:
        song = RandomLyrics[0]
        date = str(RandomLyrics[1])
        lyric = str(RandomLyrics[2])
        
        # lyric = lyric + "\n"  + song + "\n" + date + "\n"
        
    return lyric

def tweet_or_lyric():
    ye_response = random.randint(1, 2)
    if ye_response == 1:
        ye_response = get_random_tweet()
    else:
        ye_response = YeRandomLyrics()
    return ye_response

print(tweet_or_lyric())

ye_says = tweet_or_lyric()
ye_says

    
