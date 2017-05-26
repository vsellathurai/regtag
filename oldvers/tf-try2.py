# -*- coding: utf-8 -*-
"""
Created on Wed May 03 15:28:41 2017

@author: vsellathurai
"""

import numpy as np
import pandas
import codecs
import os
import re
import mainvick as m

#REGEX = re.compile(r" \s*")
def tokenize(list_of_all_papers):
    return list_of_all_papers.strip().lower().split()

cleanwords=[tokenize(x) for x in m.list_of_all_papers]