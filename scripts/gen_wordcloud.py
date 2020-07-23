#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python program to generate WordCloud """

import os
# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
#import pandas as pd
import markdown
from bs4 import BeautifulSoup
#import random

# Reads text from 'README.md' file
filename="README.md"
if not os.path.isfile(filename):
	filename = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

if os.path.isfile(filename):
	readme = markdown.markdown(open(filename).read())
	#print (BeautifulSoup(html, 'html5lib').text)
	comment_words = BeautifulSoup(readme, 'html5lib').text.lower()

	filename="experience.txt"
	if not os.path.isfile(filename):
		filename = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

	if os.path.isfile(filename):
		experience = markdown.markdown(open(filename).read())
		#print (BeautifulSoup(html, 'html5lib').text)
		comment_words = comment_words + BeautifulSoup(experience, 'html5lib').text.lower()

	filename="experience.txt"
	if not os.path.isfile(filename):
		filename = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

	stopwords = set(STOPWORDS)
	if os.path.isfile(filename):
		text_file = open("stopwords.txt", "r")
		for line in text_file:
			stopwords.add(line.strip('\n'))
	#comment_words = comment_words + open("../Resume.txt").read()
	#stopwords.update(["currently", "using", "here", "set", "at", "project", "click", "high", "busy", "small", "dl", "base"])

	wordcloud = WordCloud(width = 1200, height = 300,
					#background_color='black', colormap='Set2',
					#background_color='white', colormap='brg',
					#background_color='black', colormap='rainbow',
					#background_color='white', colormap='Oranges_r',
					#background_color='black', colormap='Spectral',
					#background_color='black', colormap='plasma',
					background_color='white', colormap='OrRd_r',
					#background_color='black', colormap='hsv_r',
					#background_color='white', colormap='Dark2',
					min_font_size = 9,
					random_state=1,
					max_words=100,
					stopwords = stopwords).generate(comment_words)
	#change the color setting

	wordcloud.to_file(os.path.dirname(os.path.abspath(__file__)) + "/../images/bannerwc.png")
else:
	print("Unable to load README.md")
