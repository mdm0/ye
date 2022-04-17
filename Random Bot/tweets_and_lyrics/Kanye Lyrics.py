import random

YeLyrics = open("Ye Lyrics.csv", "r")
ReadLyrics = YeLyrics.readlines()

def YeRandomLyrics():
    RandomLyrics = random.choice(ReadLyrics[1:])
    RandomLyrics = RandomLyrics.split(",")
    
    for lyric in RandomLyrics:
        song = RandomLyrics[0]
        date = str(RandomLyrics[1])
        lyric = str(RandomLyrics[2])
        
        lyric = lyric + "\n"  + song + "\n" + date + "\n"
        
    return lyric

def ReturnLyrics():
    GetLyrics = True
    while GetLyrics == True:
        print(YeRandomLyrics())
        GetLyrics = input("I know I'm a lyrical genius. Want to hear more of my genius? Y/N \n")
        if GetLyrics == "n" or GetLyrics == "N":
            GetLyrics = False
            return False
        else:
            GetLyrics = True

ReturnLyrics()
