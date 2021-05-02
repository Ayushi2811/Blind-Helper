# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:40:00 2021

@author: Ayushi Chauhan
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
from gtts import gTTS
import os
text='hey!how are you all.Hope u all are fine and in a good condition.??'
# using English language as output
language = 'en' #english
speech = gTTS(text = text, lang = language, slow = False)
# saving the audio file in mp3 format
speech.save('english_samples.mp3')
#to play string in wav
os.system('english_samples.mp3')
