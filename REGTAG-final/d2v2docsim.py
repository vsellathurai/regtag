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

#Reading the train & test corpus and doing basic pre-processing to split the file up into small sentences.
def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

#Specifying training and testing sets. The training set contains paragraphs from the MiFID document.
#The test set comprises of consultation papers & news stories
train_corpus = list(read_corpus(lee_train_file))
test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

#Calling the model and training it
model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=10, workers = 30)
model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count)

#Listing the baseline threshold for Cosine Similarity and the cosultation paper in question.
#These are the 2 adjustable variables
threshold = 0.2
cp_id = 78

#Creating a matrix of cosine simialrity between consultation papers based on trained model using MiFID
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
        
#Converting the matrix into a dataframe
ranked = pd.DataFrame(second_ranks)

#Dropping the NaNs and organising the consine similarities and docids for easy call back
sr = ranked[cp_id].sort_values(ascending=False).dropna()
srs = sr.index

#Printing end results
print 'Document ' + str(cp_id) + ':' + '\n' 
print m.list_of_all_papers[cp_id] + '\n'
print 'Top 3 Cosine Similarity - Document ID & Cosine Similarity'
print str(sr[1:4]) + '\n'
print 'Best Matched Document:' + m.list_of_all_papers[srs[1]]  + '\n'
print '2nd Best Matched Document:' + m.list_of_all_papers[srs[2]]  + '\n'
print '3rd Best Matched Document:' + m.list_of_all_papers[srs[3]]  + '\n'


