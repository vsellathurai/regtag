class ProdClassifier:

    def __init__(self, list_of_all_papers, buckets):
        self.list_of_all_papers=list_of_all_papers
        self.buckets=buckets
    
    def MyClassifier(self):
        
        #Trading
        Bloomberg_SEF=["dodd-frank","swap","dodd","frank","sef","execution","reporting","trade",
                       "reporting","mandatory","trading","clearing","e-trading"]
        DL_Covered_Funds_Package=["volcker","covered funds","covered"]
        Bloomberg_MARS=["derivatives","scenario analysis","pre-trade","trades","otc","scenario",
                        "analysis","volcker","mifid","sec","15c-3-5","finrag"]
        Bloomberg_BTCA=["execution","surveillance","transaction","behavior","requirement"]
        SWPM_BCOL=["collateral","clearing","bilateral","csa","calculation"]
        Bloomberg_CVA=["cva","credit","gaap","ifrs"]
        Collateral_Calculation=["collateral","margin"]
        
        #Risk and Capital Management
        Bloomberg_SCR_Calculation=["solvency","risk","liability","calculation"]
        SSFA_Tool=["capital", "collateral", "ssfa"]
        Bloomberg_Enterprise_Risk=["crisis", "stress", "ccar", "finra","risk"]
        DL_HQLA_Package=["lcr", "liquidity", "quality", "liquid", "hqla","assets","high quality"]
        Bloomberg_LQA_Tool=["market","valuation","monitoring","liquidity"]
        
        #Regulatory and Accounting reporting
        Bloomberg_Hedge_Accounting_Solutions=["hedging","accounting","loss"]
        Bloomberg_FVHL_DL_Transparency_Tool=["measure","measurement","values", "transparency","fair"]
        BVAL=["pricing","methodology","evaluation"]
        EMIR=["repositories", "reporting","report"]
        Bloomberg_Trading_Solutions=["trading system","platform","electronic","e-trading","system"]
        
        #Compliance
        BVAULT=["compliance", "secure", "monitoring","legal"]
        Bloomberg_Legal_Entity_Reference_Database=["kyc","sanctions","aml","legal"]
        Bloomberg_TAX_solutions=["tax"]
        Bloomberg_Tradebook=["broker", "commission","research"]
        Bloomberg_Trading_Solutions=["market", "access","trade","trading"]
        
        # loop through to get products
        list_of_all_papers=self.list_of_all_papers
        buckets=self.buckets
        
        products=[]
        
        for i in range(len(list_of_all_papers)):
            
            temp_prod=[]
            
            if "Trading" in buckets[i]:
                if any(word in list_of_all_papers[i] for word in Bloomberg_SEF):
                    temp_prod.append("Bloomberg SEF")
                if any(word in list_of_all_papers[i] for word in DL_Covered_Funds_Package):
                    temp_prod.append("DL Covered Funds Package")
                if any(word in list_of_all_papers[i] for word in Bloomberg_MARS):
                    temp_prod.append("Bloomberg MARS")
                if any(word in list_of_all_papers[i] for word in Bloomberg_BTCA):
                    temp_prod.append("Bloomberg BTCA")
                if any(word in list_of_all_papers[i] for word in SWPM_BCOL):
                    temp_prod.append("SWPM<GO>/BCOL<GO>")
                if any(word in list_of_all_papers[i] for word in Bloomberg_CVA):
                    temp_prod.append("CVA")
                if any(word in list_of_all_papers[i] for word in Collateral_Calculation):
                    temp_prod.append("Collateral Calculation")
                else:
                    temp_prod.append("Bloomberg Trading Solutions")
                
                
            if "Risk & Capital Management" in buckets[i]:
                if any(word in list_of_all_papers[i] for word in Bloomberg_SCR_Calculation):
                    temp_prod.append("Bloomberg SCR Calculation")
                if any(word in list_of_all_papers[i] for word in SSFA_Tool):
                    temp_prod.append("SSFA Tool")
                if any(word in list_of_all_papers[i] for word in Bloomberg_Enterprise_Risk):
                    temp_prod.append("Bloomberg Enterprise Risk")
                if any(word in list_of_all_papers[i] for word in DL_HQLA_Package):
                    temp_prod.append("DL HQLA Package")
                if any(word in list_of_all_papers[i] for word in Bloomberg_LQA_Tool):
                    temp_prod.append("Bloomberg LQA Tool")
                else:
                    temp_prod.append("ERSK Desktop Solution")
                
            if "Regulatory & Accounting Reporting" in buckets[i]:
                if any(word in list_of_all_papers[i] for word in Bloomberg_Hedge_Accounting_Solutions):
                    temp_prod.append("Bloomberg Hedge Accounting Solutions")
                if any(word in list_of_all_papers[i] for word in Bloomberg_FVHL_DL_Transparency_Tool):
                    temp_prod.append("Bloomberg FVHL DL Transparency Tool")
                if any(word in list_of_all_papers[i] for word in BVAL):
                    temp_prod.append("BVAL")
                if any(word in list_of_all_papers[i] for word in EMIR):
                    temp_prod.append("EMIR")
                if any(word in list_of_all_papers[i] for word in Bloomberg_Trading_Solutions):
                    temp_prod.append("Bloomberg Trading Solutions")
                else:
                    temp_prod.append("Trading System Regulatory Reporting")
                        
            if "Compliance" in buckets[i]:
                if any(word in list_of_all_papers[i] for word in BVAULT):
                    temp_prod.append("BVAULT")
                if any(word in list_of_all_papers[i] for word in Bloomberg_Legal_Entity_Reference_Database):
                    temp_prod.append("Bloomberg Legal Entity Reference Database")
                if any(word in list_of_all_papers[i] for word in Bloomberg_TAX_solutions):
                    temp_prod.append("Bloomberg TAX solutions")
                if any(word in list_of_all_papers[i] for word in Bloomberg_Tradebook):
                    temp_prod.append("Bloomberg Tradebook")
                if any(word in list_of_all_papers[i] for word in Bloomberg_Trading_Solutions):
                    temp_prod.append("Bloomberg Trading Solutions")
                else:
                    temp_prod.append("Compliance Desktop Solutions")
            
            products.append(temp_prod)
        return(products)
