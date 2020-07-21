#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python program to generate WordCloud """

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
#import pandas as pd
import markdown
from bs4 import BeautifulSoup
#import random

# Reads text from 'README.md' file
html = markdown.markdown(open("../README.md").read())
#print (BeautifulSoup(html, 'html5lib').text)
comment_words = BeautifulSoup(html, 'html5lib').text.lower()
#comment_words = comment_words + open("../Resume.txt").read()
stopwords = set(STOPWORDS)
stopwords.update(["currently", "using", "here", "set", "at", "project", "click", "high"])

wordcloud = WordCloud(width = 1200, height = 300,
				background_color='white',
				#colormap='Set2',
				colormap='rainbow',
				min_font_size = 9,
				random_state=1,
                max_words=50,
				stopwords = stopwords).generate(comment_words)
#change the color setting
#wordcloud.recolor(color_func = grey_color_func)

wordcloud.to_file("../images/bannerwc.png")
