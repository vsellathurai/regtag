# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:01:59 2017

@author: vsellathurai
"""

import gensim
import os
import collections
import smart_open
import random
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import main as m

# Set file names for train and test data
test_data_dir = scriptdir = os.path.dirname(os.path.realpath(__file__))
lee_train_file = test_data_dir + os.sep + 'train.cor'
lee_test_file = test_data_dir + os.sep + 'test_corpus.cor'

#Reading the train & test corpus into 
def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])
                
train_corpus = list(read_corpus(lee_train_file))
test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=10, workers = 30)

model.build_vocab(train_corpus)

model.train(train_corpus, total_examples=model.corpus_count)

second_ranks = []
for doc_id_i in range(len(m.list_of_all_papers)):
        ranks = []
        for doc_id_j in range(len(m.list_of_all_papers)):
            sims = model.docvecs.similarity_unseen_docs(model, m.list_of_all_papers[doc_id_j],m.list_of_all_papers[doc_id_i])
            if sims > threshold:
                ranks.append(sims)
            else:
                ranks.append(np.nan)
        second_ranks.append(ranks)

ranked = pd.DataFrame(second_ranks)

threshold = 0.2
cp_id = 50

sorted_ranks = ranked[cp_id].sort_values(ascending=False).dropna()
sorted_ranks = sorted_ranks.loc[:]
print sorted_ranks

print 'Document no.'+ str(cp_id) + ':' + str(ranked[cp_id].sort_values())  

