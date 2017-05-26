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
import utils2 as u2

# Set file names for train and test data
test_data_dir = scriptdir = os.path.dirname(os.path.realpath(__file__))
lee_train_file = test_data_dir + os.sep + 'test_corpus.cor'
lee_test_file = test_data_dir + os.sep + 'train_corpus.cor'


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

model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=55)

model.build_vocab(train_corpus)

model.train(train_corpus, total_examples=model.corpus_count)

ranks = []
second_ranks = []
for doc_id in range(len(train_corpus)):
    inferred_vector = model.infer_vector(train_corpus[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)
    
    second_ranks.append(sims[1])
    
collections.Counter(ranks)

print('Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))
    
