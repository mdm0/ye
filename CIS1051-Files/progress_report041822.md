# 04/18/22 Progress Report on Ye Say
Michael's take: 
## The Good
I combined my work with Abby's and followed a [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to turn our datasets into a chat bot that delivers a random Kanye tweet or lyric. Ye Say's [website](https://yesay.netlify.app) also looks fantastic. It runs off of Netlify and GitHub Pages.  
## Giving Ye a Brain
A couple of people asked me if I'd consider adding AI to Ye Say, rather than the bot just giving a random response. I got a .txt file of Kanye's lyrics from [Kaggle](https://www.kaggle.com/datasets/convolutionalnn/kanye-west-lyrics-dataset) and coded a small program to pare it down and convert it into a .csv. Since I know virtually nothing about AI development, I followed this [tutorial](https://www.freecodecamp.org/news/discord-ai-chatbot/) and used the resources that it included to create a bot and Kanye AI model (based on Microsoft's DialoGPT), which is hosted on [HuggingFace](https://huggingface.co/mdm).  
## The Bad
Not enough RAM allocated on Colab to work with my entire dataset, so I used the first 800 verses on the spreadsheet to make my model. I thought that my program did a good enough job of filtering Kanye's lyrical genius, but after running the bot, it has become apparent that I still need to weed out some *choice* words.  
Oh yeah, the Ye AI is kind of mean. 
## The Future
Exploring hosting the bot on [repl.it](https://repl.it) and using a tool to run it continuously so that Ye Say can be used at any time.
