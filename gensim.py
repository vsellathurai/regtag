# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:38:09 2017

@author: vsellathurai
"""

from gensim.models import doc2vec
import mainvickfinal as m

fn = m.list_of_all_papers
model = doc2vec.Doc2Vec.load(fn)
model.most_similar('pregnant')
matches = list(filter(lambda x: 'SENT_' in x[0], matches))