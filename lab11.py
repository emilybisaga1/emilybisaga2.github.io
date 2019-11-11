'''
INSTRUCTIONS:
Just like lab 10, today's lab has no doctests for you to complete.
Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive
Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        The 2018 file actually also includes tweets from 2019 and is updated hourly.
Step 3: Unzip each of these files to get files that look like `condensed_*.json`.
Step 4: Write a python program that:
    1. Opens each file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.
    2. Prints the total number of tweets.
    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many 
       different capitalizations, and your program should count the word 
       no matter how it is capitalized.  For example, `OBAMA`, `obama`, and `ObAmA`
       all need to count as an occurance of the word `Obama`.
    4. Prints out a count of each of these words.
My program ran on all tweets as of 7AM on 24 October 2019 gives the output
    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333,
    'mexico': 199}
Your program should give the same numbers (or possibly a few higher if Trump sends new tweets over the next few days).
========================================
EXTRA CREDIT:
You may earn up to 3 points of extra credit on this lab if you also:
    1. select at least 3 more interesting words/phrases to count in trump's tweets,
    2. calculate the percentage of tweets that contain each word, and
    3. display them nicely.
The display must have all words right justified and the percents printed with two 
significant figures (on both sides of the decimal) as shown in the example output below.
    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
'''
import string
import json
trump = 0
russia=0
obama=0
fake_news=0
mexico=0
length = 0

# for 2009 
with open('condensed_2009.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
for info in tweets:
    length += 1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

#for 2010
with open('condensed_2010.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

#for 2011
with open('condensed_2011.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1
    
#for 2012
with open('condensed_2012.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

        
#for 2013
with open('condensed_2013.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1   
    
        
#for 2014
with open('condensed_2014.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

#for 2015
with open('condensed_2015.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

#for 2016
with open('condensed_2016.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1
        
#for 2017
with open('condensed_2017.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
        if words_list[i] == 'russia':
            russia+=1
        if words_list[i] == 'obama':
            obama+=1
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
        if words[i] == 'mexico':
            mexico+=1
        i+=1

#for 2018
with open('condensed_2018.json','r') as f:
    text = f.read()
    tweets = json.loads(text)
    
for info in tweets:
    length +=1
    words = info['text']
    import string
    table = str.maketrans(dict.fromkeys(string.punctuation))
    words = words.translate(table)
    words_list = []
    words_list = words.lower().split(" ")
    #print(words_list)
    i=0
    while i < len(words_list):
        if words_list[i] == 'trump':
            trump+=1
            #print('word', words_list[i])
        if words_list[i] == 'russia':
            russia+=1
            #print('word', words_list[i])
        if words_list[i] == 'obama':
            obama+=1
           # print('word', words_list[i])
        if words_list[i-1] == 'fake' and words_list[i] == 'news':
            fake_news+=1
           # print('word', words_list[i-1], words_list[i])
        if words[i] == 'mexico':
            mexico+=1
          #  print('word', words_list[i])
        i+=1


print('length=', length)
counts = {'trump': trump, 'russia': russia, 'obama': obama, 'fake news': fake_news,
    'mexico': mexico}
print('counts=', counts)
