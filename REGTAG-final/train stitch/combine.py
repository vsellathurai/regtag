# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:50:33 2017

@author: vsellathurai
"""
import os

scriptdir = os.path.dirname(os.path.realpath(__file__))

import glob

read_files = glob.glob("*.txt")

with open("train.cor", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())