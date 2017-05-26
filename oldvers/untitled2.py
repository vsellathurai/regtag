# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:32:47 2017

@author: vsellathurai
"""
import codecs
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas

import mainvick as m

tf= TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
tfidf_matrix =  tf.fit_transform(m.cleanwords)
feature_names = tf.get_feature_names() 
dense = tfidf_matrix.todense()

master = []
cp = dense[1].tolist()[0]
f_score = [pair for pair in zip(
range(0, len(cp)), cp) if pair[1] > 0]
sorted_f_score = sorted(f_score, key=lambda t: t[1] * -1)
master.append(sorted_f_score)

for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_f_score][:20]:
    print('{0: <50} {1}'.format(phrase, score))