# pip3 install requests

import requests
from bs4 import BeautifulSoup

#here we are sample coding a webpage

html='''
<title>example</title>
<p>this is an example.</p>
<p>this is also an example. </p>
<ol>
<li><a href='ur1'>elem1</a></li>
<li><a href='ur2'>elem2</a></li>
<li><a href='ur3'>elem3</a></li>
</ol>
'''

bs=BeautifulSoup(html)

for a in bs.find_all('a'):
    print('a.attrs=', a.attrs)
    
'''
bs.find('') finds only the first, gives you beautoufl soup objet 
bs.find_all('') finds all the examples and gives you a list

bs.find('a').attrs
{'href': 'ur1'} // keys as attributes and avlues as vallues

bs.find('a').text
'elem1'

bs.find('a').contents
['elem1']b

bs.find('ol').text
'\nelem1\nelem2\nelem3\n'   // shows the new lines
-does not return a list, text returns a string!!

bs.find('ol').contents
-gives tou everything, does not remove html 


'''
## notes from Oct 15#

webpage = requests.get('https://en.wikipedia.org/wiki/Super_Fly_(1972_film)')

bsnew=BeautifulSoup(webpage.text)
print('text=', bsnew.text)
