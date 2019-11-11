import json
import matplotlib.pyplot as plt
import numpy as np
import math

#loading big bang info
with open('big bang.json','r') as f:
    text=f.read()
    bang=json.loads(text)

#getting data for number of episodes per season
season_one_numb = 0
i=0
stats =[]

for item in bang["_embedded"]["episodes"]:
    if (bang["_embedded"]["episodes"][i]["season"]) == 1:
        info = {}
        season_one_numb+=1
        info['number'] = (bang["_embedded"]["episodes"][i]["number"])
        if "Penny" in bang["_embedded"]["episodes"][i]["summary"]:
            info['Penny'] = 1
        if "Sheldon" in bang["_embedded"]["episodes"][i]["summary"]:
            info['Sheldon'] = 1
        stats.append(info)
    i+=1
    if i == 278:
	    break


#plot results for big bang
N = 17
penny_number= (1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1)
sheldon_number=(1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0)
ind = np.arange(N)
width= 0.35
plt.bar(ind, penny_number, width, label='Penny')
plt.bar(ind + width, sheldon_number, width,
    label='Sheldon')

plt.ylabel('Is the epidsode about the character')
plt.xlabel('Episode Number')
plt.title('Looking at presence of Penny and Sheldon in season one')

plt.xticks(ind + width / 2, ('1', '2','3', '4',
                             '5', '6', '7','8','9',
                             '10','11', '12', '13',
                             '14', '15', '16', '17'))

plt.legend(loc='best')
plt.show()
##################################################################################################################

# loading black mirror info
with open('shows.json','r') as f:
    text=f.read()
    mirror=json.loads(text)

#getting data for number of episodes per season
season_one_runtime=0
season_one_eps=0
season_two_runtime=0
season_two_eps=0
season_three_runtime=0
season_three_eps=0
i=0

for item in mirror["_embedded"]["episodes"]:
    if (mirror["_embedded"]["episodes"][i]["season"]) == 1:
        season_one_runtime+= mirror["_embedded"]["episodes"][i]["runtime"]
        season_one_eps+=1
    if (mirror["_embedded"]["episodes"][i]["season"]) == 2:
        season_two_runtime+= mirror["_embedded"]["episodes"][i]["runtime"]
        season_two_eps+=1
    if (mirror["_embedded"]["episodes"][i]["season"]) == 3:
        season_three_runtime+= mirror["_embedded"]["episodes"][i]["runtime"]
        season_three_eps+=1
    i+=1
    if i == 278:
	    break
avgs={}
avgs['season1'] = (season_one_runtime/season_one_eps)
avgs['season2'] = (season_two_runtime/season_two_eps)
avgs['season3'] = (season_three_runtime/season_three_eps)

#plotting data
plt.style.use('ggplot')
x = ['season1', 'season2', 'season3']
y = [avgs['season1'], avgs['season2'], avgs['season3']]
plt.plot(x, y)
plt.xlabel("Season")
plt.ylabel("Average runtime")
plt.title("Looking at the Average Runtime for Black Mirror Seasons 1-3")
plt.show()

