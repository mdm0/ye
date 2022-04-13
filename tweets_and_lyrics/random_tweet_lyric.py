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
        
        tweet = tweet + "\n"  +  full_date + "\n"
        
    return tweet

def return_tweet():
    load_tweet = True
    while load_tweet == True:
        print(get_random_tweet())
        load_tweet = input("Another one? Y/N \n")
        if load_tweet == "n" or load_tweet == "N":
            load_tweet = False
            return False
        else:
            load_tweet = True

return_tweet()
