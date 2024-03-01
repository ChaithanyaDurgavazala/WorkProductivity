import pandas as pd
import pkg_resources
import cas_rn_validator.validator as v


'''
Function to search ChemicalFormula With CAS NUMBER
'''
def getChemicalFormulaWithCAS(input_str):
    # validate cas registry number
    if v.validateCAS_RN(input_str)==True:
        # exception handling for wrong cas_rn dataset file format
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['CAS_Number']==input_str]
                    return df['Chemicalformula'].tolist()[0]
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)

    else:
        return None      


'''
Function to search Synonyms With CAS NUMBER
'''
def getSynonymsWithCAS(input_str):
    # validate cas registry number
    if v.validateCAS_RN(input_str)==True:
        # exception handling for wrong cas_rn dataset file format
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['CAS_Number']==input_str]
                    return df['Synonyms'].tolist()[0]
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)
    else:
        return None      


'''
Function to search CASNumber With Synonyms
'''
def getCASNumberWithSynonyms(input_str):
        # exception handling for wrong cas_rn dataset file format    
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['Synonyms']==input_str]
                    if len(df)>0:
                        return df['CAS_Number'].tolist()[0]
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search ChemicalFormula With Synonyms
'''
def getChemicalFormulaWithSynonyms(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    # reading csv and getting data
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    df=pd.read_csv(stream)
                    df=df[df['Synonyms']==input_str]
                    if len(df)>0:
                        return df['Chemicalformula'].tolist()[0]
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search CASNumber With ChemicalFormula
'''
def getCASNumberWithChemicalFormula(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    # reading csv and getting data
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    df=pd.read_csv(stream,encoding='cp1252')
                    df=df[df['Chemicalformula']==input_str]
                    if len(df)>0:
                        return df['CAS_Number'].tolist()[0]
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search Synonyms With ChemicalFormula
'''
def getSynonymsWithChemicalFormula(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    # reading csv and getting data
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    df=pd.read_csv(stream,encoding='cp1252')
                    df=df[df['Chemicalformula']==input_str]
                    if len(df)>0:
                        return df['Synonyms'].tolist()[0]
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search Chemicalformula by CAS Number
'''
def searchChemicalFormulaWithCAS(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    # reading csv and getting data
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    df=pd.read_csv(stream)
                    dfContainsWithList=df[df['CAS_Number'].str.contains(input_str,regex=False)]['Chemicalformula'].values.tolist()
                    dfstartsWithList=df[df['CAS_Number'].str.startswith(input_str)]['Chemicalformula'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search Synonyms by CAS Number
'''
def searchSynonymsWithCAS(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    dfContainsWithList=df[df['CAS_Number'].str.contains(input_str,regex=False)]['Synonyms'].values.tolist()
                    dfstartsWithList=df[df['CAS_Number'].str.startswith(input_str)]['Synonyms'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search CAS Number by Synonyms
'''
def searchCASNumberWithSynonyms(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    dfContainsWithList=df[df['Synonyms'].str.contains(input_str,regex=False)]['CAS_Number'].values.tolist()
                    dfstartsWithList=df[df['Synonyms'].str.startswith(input_str)]['CAS_Number'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search ChemicalFormula by Synonyms
'''
def searchChemicalFormulaWithSynonyms(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    dfContainsWithList=df[df['Synonyms'].str.contains(input_str,regex=False)]['Chemicalformula'].values.tolist()
                    dfstartsWithList=df[df['Synonyms'].str.startswith(input_str)]['Chemicalformula'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search CASNumber by ChemicalFormula 
'''
def searchCASNumberWithChemicalFormula(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    dfContainsWithList=df[df['Chemicalformula'].str.contains(input_str,regex=False)]['CAS_Number'].values.tolist()
                    dfstartsWithList=df[df['Chemicalformula'].str.startswith(input_str)]['CAS_Number'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search Synonyms by ChemicalFormula
'''
def searchSynonymsWithChemicalFormula(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                # making stream for fetching datset from data folder
                if((entry.split('.')[-1])=='csv'):
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream,encoding='cp1252')
                    dfContainsWithList=df[df['Chemicalformula'].str.contains(input_str,regex=False)]['Synonyms'].values.tolist()
                    dfstartsWithList=df[df['Chemicalformula'].str.startswith(input_str)]['Synonyms'].values.tolist()
                    if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
                        dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
                        return dfstartsWithList
                    elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
                        return dfContainsWithList
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search by CAS NUMBER
'''
def search_by_cas_number(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['CAS_Number'].str.contains(input_str,regex=False)]
                    if len(df)>0:
                        return df.values.tolist()
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search by Synonyms
'''
def search_by_synonyms(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['Synonyms'].str.contains(input_str,regex=False)]
                    if len(df)>0:
                        return df.values.tolist()
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)


'''
Function to search by Chemicalformula
'''
def search_by_chemicalformula(input_str):
        # exception handling for wrong cas_rn dataset file format 
        try:
            for entry in pkg_resources.resource_listdir('CAS_RN_Validator.src.cas_rn_validator', 'data'):
                if((entry.split('.')[-1])=='csv'):
                    # making stream for fetching datset from data folder
                    stream = pkg_resources.resource_stream(__name__, 'data\\'+entry)
                    # reading csv and getting data
                    df=pd.read_csv(stream)
                    df=df[df['Chemicalformula'].str.contains(input_str,regex=False)]
                    if len(df)>0:
                        return df.values.tolist()
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)

