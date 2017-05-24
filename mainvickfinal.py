# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 17:42:15 2017

@author: vsellathurai
"""

import codecs
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas

# country directory
mydir="C:\\Users\\VickSella\\Desktop\\regtag\\REG Dump"
root, country_dir, files = next(os.walk(mydir))
#country_dir = ["Australia","China","Hong Kong","New Zealand"]
# loop through country directories
all_country = []
all_country_res = []

# read files from directory folders
mydata=[]
header=[]

mydir="C:\\Users\\VickSella\\Desktop\\regtag\\REG Dump"

# country loop to the end
for country in country_dir:
    
    currentdir = mydir+"\\"+country
    os.chdir(currentdir)
    
for filename in os.listdir(currentdir):
    f = codecs.open(filename, 'r', 'ascii', 'ignore')
    text=[rows for rows in f]
    mydata.append(text)
    header.append(filename)
    all_country.append(country)
    
def preprocess(full_text):
        full_text=[str(x) for x in full_text] #remove unicode format
        full_text=' '.join(full_text)
        full_text=re.sub('[^A-Za-z0-9]+', ' ', full_text) #remove special characters 
        full_text=full_text.lower() #convert to lower case
        return(full_text)
    
list_of_all_papers=[preprocess(paper) for paper in mydata]


def tokenize(list_of_all_papers):
    return list_of_all_papers.strip().lower().split()
    
cleanwords=[tokenize(x) for x in list_of_all_papers]




    
