# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:38:09 2017

@author: vsellathurai
"""
import gensim
import os
import collections
import smart_open
import random
import mainvickfinal2 as m

train_corpus = list(m.cleanwords[:10])

model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=55)
model.build_vocab(train_corpus)

