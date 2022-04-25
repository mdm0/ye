Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
import discord
import random

import tweets_and_lyrics.random_tweet_lyric as yesays

#Pete Davidson Response
pete_response = "God saved me from that crash just so I can beat Pete Davidson's ass " #Lyric from 'Eazy'

#Kim K Response
kim_response = "..."

#Taylor Swift Response
def taylor_swift():
    r1 = "Yo Taylor, I'm really happy for you, I'mma let you finish, but Beyoncé had one of the best videos of all time"
    r2 = "I’M GOING TO PERSONALLY SEE TO IT THAT TAYLOR SWIFT  GETS HER MASTERS BACK.   SCOOTER IS A CLOSE FAMILY FRIEND" #Tweet from @KanyeWest 9/18/2020 @ 16:20
    r3 = "Not gonna use a snake emoji cause you know why ...  I’m not sure if Christians are allowed to use snake emojis    🤔"
    pick_taylor_response = random.randint(1,3)
    if pick_taylor_response == 1:
        pick_taylor_response = r1
    if pick_taylor_response == 2:
        pick_taylor_response = r2
    if pick_taylor_response == 3:
        pick_taylor_response = r3

    return pick_taylor_response


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
        
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if 'pete' in message.content or 'Pete' in message.content:
        await message.channel.send(
            pete_response
        )
    elif 'kim' in message.content or 'Kim' in message.content:
        await message.channel.send(
            kim_response
        )
    elif 'taylor' in message.content or 'Taylor' in message.content:
        await message.channel.send(
            taylor_swift()
        )
    else:
        await message.channel.send(
            random_tweet_lyric.tweet_or_lyric()
        )
            
# client.run('') insert your Discord API Key Here
