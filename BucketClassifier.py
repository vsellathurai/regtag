# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:25:59 2017

@author: mlin171
"""

class BucketClassifier:
    
    def __init__(self, list_of_all_papers):
        self.list_of_all_papers = list_of_all_papers
        
    def MyClassifier(self):
        
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
                             
         def to_lower(list_of_words):
             return([x.lower() for x in list_of_words])
         
         keyword_trading=to_lower(keyword_trading)
         keyword_risk_cap_mgt=to_lower(keyword_risk_cap_mgt)
         keyword_reg_acct_rep=to_lower(keyword_reg_acct_rep)
         keyword_compliance=to_lower(keyword_compliance)
         
         def word_count(list_of_all_papers, keyword_list):
             return([sum(1 for word in keyword_list if word in sentence) for sentence in list_of_all_papers])
             
         trading=word_count(self.list_of_all_papers, keyword_trading)
         risk_cap_mgt=word_count(self.list_of_all_papers, keyword_risk_cap_mgt)
         reg_acct_rep=word_count(self.list_of_all_papers, keyword_reg_acct_rep)
         compliance=word_count(self.list_of_all_papers, keyword_compliance)
         
         res1=zip(trading,risk_cap_mgt,reg_acct_rep,compliance)
         
         # assign to bucket
         # note the sequence of the buckets: 
         # 1-Trading 2-Risk & Capital Management 3-Regulatory & Accounting Reporting 4-Compliance 
         lookup_buckets=["Trading", "Risk & Capital Management", "Regulatory & Accounting Reporting", "Compliance"]
         buckets=[]
         
         for x in res1:
             max_freq=max(x)
             temp_index=[i for i in range(len(x)) if x[i] == max_freq]
             temp_bucket=[lookup_buckets[j] for j in temp_index]
             buckets.append(temp_bucket)
         
         return(trading,risk_cap_mgt,reg_acct_rep,compliance,buckets)