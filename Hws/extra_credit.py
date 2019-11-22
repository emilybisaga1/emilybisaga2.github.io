def generate_wordcloud(text):
    '''
    You can earn up to 10 points of extra credit by implementing this function,
    but you are not required to implement this function if you do not want the extra credit.
    To get the extra credit, this function should take as input a string
    and save a file to your computer called `wordcloud.png`.
    The word cloud should be generated using python's wordcloud library from the text input.
    You can find instructions on how to install and use wordcloud online at
    https://github.com/amueller/word_cloud
    '''
import os

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = 'laika space soviet dogs dog sputnik time mission laikas launch flight russian moscow scientists animals died november one spacecraft rocket'

wordcloud = WordCloud().generate(tet)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
