# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:08:29 2017

@author: mlin171
"""

import codecs
import re
import os
#os.chdir("F:\\Python docs\\AREG\\test2")
#from BucketClassifier import BucketClassifier
#from ProdClassifier import ProdClassifier
os.chdir("C:\\Users\\VickSella\\Desktop\\regtag\\REGTAG-final")

###############################################################################
# country directory
mydir="C:\\Users\\VickSella\\Desktop\\regtag\\REGTAG-final"
root, country_dir, files = os.walk(mydir).next()
#country_dir = ["Australia","China","Hong Kong","New Zealand"]
# loop through country directories
all_country = []
all_country_res = []

# country loop to the end
for country in country_dir:
    
    currentdir = mydir+"\\"+country
    os.chdir(currentdir)
    
    # read files from directory folders
    mydata=[]
    header=[]
    
    for filename in os.listdir(currentdir):
        f = codecs.open(filename, 'r', 'ascii', 'ignore')
        text=[rows for rows in f]
        mydata.append(text)
        header.append(filename)
        all_country.append(country)

    # Extract SUID
    #SUIDs=[str(x[0]) for x in mydata]
    #SUIDs=[x.rstrip() for x in SUIDs]
    
    def preprocess(full_text):
        full_text=[str(x) for x in full_text] #remove unicode format
        full_text=' '.join(full_text)
        full_text=re.sub('[^A-Za-z0-9]+', ' ', full_text) #remove special characters 
        full_text=full_text.lower() #convert to lower case
        return(full_text)
    
    list_of_all_papers=[preprocess(paper) for paper in mydata]
    
#    bucket = BucketClassifier(list_of_all_papers)
#    res_bucket = bucket.MyClassifier()
#    #return(trading,risk_cap_mgt,reg_acct_rep,compliance,buckets)
#    buckets = res_bucket[4]
#
#    prod = ProdClassifier(list_of_all_papers,buckets)
#    res_prod = prod.MyClassifier()
#    #return(product)
#    
#    trading=res_bucket[0]
#    risk_cap_mgt=res_bucket[1]
#    reg_acct_rep=res_bucket[2]
#    compliance=res_bucket[3]
#    
#    res_final = zip(trading, risk_cap_mgt, reg_acct_rep, compliance, buckets, res_prod, all_country)
#    
#    all_country_res.append(res_final)
    