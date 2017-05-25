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
import gensim

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
    for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])
#    text=[rows for rows in f]
#    mydata.append(text)
#    header.append(filename)
#    all_country.append(country)
#    
#
#    
#def preprocess(full_text):
#        full_text=[str(x) for x in full_text] #remove unicode format
#        full_text=' '.join(full_text)
#        full_text=re.sub('[^A-Za-z0-9]+', ' ', full_text) #remove special characters 
#        full_text=full_text.lower() #convert to lower case
#        return(full_text)
#    
#list_of_all_papers=[preprocess(paper) for paper in mydata]
#
#def mk_split(paperlist):
#    gensim.utils.simple_preprocess(paperlist)
    
#proswords = [mk_split(paperlist)]       
#train_corpus = list(train)
#for i in range(81, len(processed_list)):
#    test_corpus.append(list(gensim.models.doc2vec.TaggedDocument(processed_list(i))))
    

#train_corpus = gensim.utils.simple_preprocess(list_of_all_papers[1])

#a=gensim.utils.simple_preprocess(list_of_all_papers)


#for i in enumerate(list_of_all_papers):
#            if list_of_all_papers[30:]:
#                gensim.utils.simple_preprocess(list_of_all_papers)
#            else:
#                # For training data, add tags
#                gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(list_of_all_papers[i]))
