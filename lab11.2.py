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
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
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
daca=0
huge=0
wall=0
length = 0
tweets = []

with open('condensed_2009.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2010.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2011.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2012.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2013.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2014.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2015.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2016.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2017.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))
with open('condensed_2018.json','r') as f:
    text = f.read()
    tweets.extend(json.loads(text))

for info in tweets:
    length += 1
    words = info['text']
    for char in "-.,\n'":
        words = words.replace(char, ' ')
    words_list = []
    words_list = words.lower().split(" ")
    i=0
    while i < len(words_list):
        if 'trump' in words_list[i]:
            trump+=1
            break
        if 'russia' in words_list[i]:
            russia+=1
            break
        if 'obama' in words_list[i]:
            obama+=1
            break
        if 'fake' in words_list[i-1] and 'news' in words_list[i]:
            fake_news+=1
            break
        if 'mexico' in words_list[i]:
            mexico+=1
            break
        if 'daca' in words_list[i]:
            daca+=1
            break
        if 'huge' in words_list[i]:
            huge+=1
            break
        if 'wall' in words_list[i]:
            wall+=1
            break
        i+=1


print('len(tweets)=', length)
counts = {'trump': trump, 'russia': russia, 'obama': obama, 'fake news': fake_news,
    'mexico': mexico}
print('counts=', counts)
print('percentage of tweets using phrase:')
print('daca      ', ':  ', '0''%.2f'%((daca/length)*100))
print('fake news ', ':  ', '0''%.2f'%((fake_news/length)*100))
print('huge      ', ':  ', '0''%.2f'%((huge/length)*100))
print('mexico    ', ':  ', '0''%.2f'%((mexico/length)*100))
print('obama     ', ':  ', '0''%.2f'%((obama/length)*100))
print('russia    ', ':  ', '0''%.2f'%((russia/length)*100))
print('trump     ', ':  ', '%.2f'%((trump/length)*100))
print('wall      ', ':  ', '0''%.2f'%((wall/length)*100))


#plot results
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x=counts.keys() # its really good not to specify but to have it more organized
y=counts.values()s
#x=['trump', 'russia', 'obama', 'fake news', 'mexico']
#y=[trump, russia, obama, fake_news, mexico]
ax.bar(x,y)
#plt.xticks(x,['trump', 'russia', 'obama', 'fake news', 'mexico'])
#plt.show()

#how to save the graph
#plt.savefig('trump_bar.png')


#obama tracking code
obama_counts={}
for info in tweets:
    year = info['created_at'][-4:]
    if 'obama' in tweet['text'.lower():
        if year in obama_counts:
            obama_counts[year]+=1
        else:
            obama_counts[year]=1
from pprint import pprint
pprint(obama_counts)
