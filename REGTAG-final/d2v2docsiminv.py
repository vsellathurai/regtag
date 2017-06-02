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
from sklearn.metrics.pairwise import cosine_similarity
import main as m

# Set file names for train and test data
test_data_dir = scriptdir = os.path.dirname(os.path.realpath(__file__))
lee_train_file = test_data_dir + os.sep + 'test_corpus.cor'
lee_test_file = test_data_dir + os.sep + 'train.cor'


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
    
    
    
    
#Part 3 - Computing similarity between test-document and training set
    
# Pick a random document from the test corpus and infer a vector from the model
ranks = []
second_ranks = []
for doc_id in range(len(m.list_of_all_papers)):
    inferred_vector = model.infer_vector(m.list_of_all_papers[doc_id].split())
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)
    second_ranks.append(sims[1])
    
    
from sklearn.metrics.pairwise import cosine_similarity

doc1index = 15
doc2index = 35

v1 = inferred_vector[doc1index].reshape(1,-1)
v2 = inferred_vector[doc2index].reshape(1,-1)

print 'Document 1:' + m.list_of_all_papers[doc1index]+ '\n'
print 'Document 2:' + m.list_of_all_papers[doc2index]
print cosine_similarity(v1,v2)

    
#Part 4: Compare Against a list of key words

"""
 Four Buckets
 """
 
keyword_trading=['pre-trade', 'execution','Dodd', 'Frank', 'SEF','Dodd-Frank', 
              'Dodd', 'Frank', 'CFTC', 'Volcker', 'MiFID', 'SEC', '15c3-5', 
              'FinfraG', 'reporting', 'trade', 'reporting', 'Mandatory', 'Trading', 
              'trade', 'clearing','clearance','electronic', 'trading','e-trading',
              'collateral', 'margin','research','conduct', 'behavior','transaction',
              'capital', 'requirement','adequacy','margin','reporting']
   
keyword_risk_cap_mgt=['risk','capital','Basel','CVA','CCAR','Stress','solvency',
                   'regulatory','stress test','Solvency II', 'reporting', 'trade reporting', 
                   'Mandatory Trading', 'clearing', 'mandatory clearing','clearance','mandatory',
                   'electronic trading','e-trading', 'collateral', 'margin','research','conduct', 
                   'behavior','research','capital requirement','capital adequacy','requirement','protection']
 
keyword_reg_acct_rep=['regulatory', 'accounting', 'reporting', 'FATCA', 'Form PF', 'PF', 'ASC 820', 
                   'IFRS 13', 'IAS', 'GAAP', 'CRD IV', 'EBA', 'prudent valuation', 'IRS', 
                   'fair value', 'value','reporting', 'trade reporting', 'Mandatory Trading', 
                   'clearing', 'mandatory clearing','clearance','electronic trading',
                   'e-trading','mandatory trading', 'collateral', 'margin','disclosure',
                   'conduct', 'behavior','tax','capital requirement','capital adequacy',
                   'mandatory','requirement','regulators']
 
keyword_compliance=['compliance', 'AIFMD', 'OATS', 'CAT', 'Finra', 'EMIR', 'KYC', 'AML',
                 'Anti-Money', 'Laundering', 'MiFID', 'regulation', 'stress test', 
                 'Order Audit Trail System', 'Dodd-Frank','reporting', 
             'trade reporting', 'Mandatory Trading', 'clearing', 'mandatory clearing',
                 'clearance','electronic trading','e-trading','mandatory trading', 
                 'collateral', 'protection','research','conduct', 'behavior','criminal',
                 'laundering','transparency','mandatory','requirement']


    
trading = model.infer_vector(keyword_trading)
compliance = model.infer_vector(keyword_compliance)
regulatory = model.infer_vector(keyword_reg_acct_rep)
risk = model.infer_vector(keyword_risk_cap_mgt)


sims = model.docvecs.most_similar([risk], topn=len(model.docvecs))


# Compare and print the most/median/least similar documents from the train corpus
print('Keywords used ({}): «{}»\n'.format('risk', ' '.join(keyword_risk_cap_mgt)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))