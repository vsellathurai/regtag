# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 13:50:06 2017

@author: mlin171
"""
import nltk
from nltk.stem.porter import PorterStemmer

class NLTKprocessor:
    
    def __init__(self, one_paper, enable_stem):
        
        '''
        enable_stem needs to be set as "YES" if stemming is to be used
        '''
        
        self.one_paper = one_paper
        self.enable_stem = enable_stem
    
    
    def MyProcessor(self):
        
        '''
        three steps to narrow down text
        1) Tokenization
        2) Stemming to remove morphological and inflexional endings
        3) POS tags 
        '''
        
        def word_feats(sents):
            
            '''
            Only words with selected POS taggs will be processed
            '''
            
            res = []
            for i in range(len(sents)):
                for j in range(len(sents[i])):
                    if sents[i][j][1] == 'JJ' or sents[i][j][1] == 'JJS'\
                    or sents[i][j][1] == 'JJR' or sents[i][j][1] == 'VB'\
                    or sents[i][j][1] == 'VBD' or sents[i][j][1] == 'VBG'\
                    or sents[i][j][1] == 'VBN' or sents[i][j][1] == 'VBP'\
                    or sents[i][j][1] == 'VBZ' or sents[i][j][1] == 'RB' \
                    or sents[i][j][1] == 'RBR' or sents[i][j][1] == 'RBS': 
                        res.append(sents[i][j][0])
            return dict([(word, True) for word in res])
        
        
        if self.enable_stem == "Y":
            
            tokens = nltk.sent_tokenize(self.one_paper)
            
            # stemming
            stems=[]
            for item in tokens:
                stems.append(PorterStemmer().stem(item))
            
            # POS taggs
            tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in stems]
            tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
            
            res=word_feats(tagged_sentences)
        
        
        elif self.enable_stem == "N":
            
            # tokenization ans POS tags without stemming
            sentences = nltk.sent_tokenize(self.one_paper)
            tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
            tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
            
            res=word_feats(tagged_sentences)
            
        return(res)
        