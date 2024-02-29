import pandas as pd
import pkg_resources
# import cas_rn_validator.validator as v
import casrnvalidator.validator as v

'''
Function to search ChemicalFormula With CAS NUMBER
'''
def getChemicalFormulaWithCAS(input_str):
    if v.validateCAS_RN(input_str)==True:
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['CAS_Number']==input_str]
        return df['Chemicalformula'].tolist()[0]
    else:
        return None      


'''
Function to search Synonyms With CAS NUMBER
'''
def getSynonymsWithCAS(input_str):
    if v.validateCAS_RN(input_str)==True:
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['CAS_Number']==input_str]
        return df['Synonyms'].tolist()[0]
    else:
        return None      


'''
Function to search CASNumber With Synonyms
'''
def getCASNumberWithSynonyms(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Synonyms']==input_str]
        if len(df)>0:
            return df['CAS_Number'].tolist()[0]
        else:
            return None 


'''
Function to search ChemicalFormula With Synonyms
'''
def getChemicalFormulaWithSynonyms(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Synonyms']==input_str]
        if len(df)>0:
            return df['Chemicalformula'].tolist()[0]
        else:
            return None 


'''
Function to search CASNumber With ChemicalFormula
'''
def getCASNumberWithChemicalFormula(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Chemicalformula']==input_str]
        if len(df)>0:
            return df['CAS_Number'].tolist()[0]
        else:
            return None 


'''
Function to search Synonyms With ChemicalFormula
'''
def getSynonymsWithChemicalFormula(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Chemicalformula']==input_str]
        if len(df)>0:
            return df['Synonyms'].tolist()
        else:
            return None 


'''
Function to search Chemicalformula by CAS Number
'''
def searchChemicalFormulaWithCAS(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['CAS_Number'].str.contains(input_str)]['Chemicalformula'].values.tolist()
        dfstartsWithList=df[df['CAS_Number'].str.startswith(input_str)]['Chemicalformula'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 

            
'''
Function to search Synonyms by CAS Number
'''
def searchSynonymsWithCAS(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['CAS_Number'].str.contains(input_str)]['Synonyms'].values.tolist()
        dfstartsWithList=df[df['CAS_Number'].str.startswith(input_str)]['Synonyms'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 


'''
Function to search CAS Number by Synonyms
'''
def searchCASNumberWithSynonyms(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['Synonyms'].str.contains(input_str)]['CAS_Number'].values.tolist()
        dfstartsWithList=df[df['Synonyms'].str.startswith(input_str)]['CAS_Number'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 


'''
Function to search ChemicalFormula by Synonyms
'''
def searchChemicalFormulaWithSynonyms(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['Synonyms'].str.contains(input_str)]['Chemicalformula'].values.tolist()
        dfstartsWithList=df[df['Synonyms'].str.startswith(input_str)]['Chemicalformula'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 


'''
Function to search CASNumber by ChemicalFormula 
'''
def searchCASNumberWithChemicalFormula(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['Chemicalformula'].str.contains(input_str)]['CAS_Number'].values.tolist()
        dfstartsWithList=df[df['Chemicalformula'].str.startswith(input_str)]['CAS_Number'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 


'''
Function to search Synonyms by ChemicalFormula
'''
def searchSynonymsWithChemicalFormula(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        dfContainsWithList=df[df['Chemicalformula'].str.contains(input_str)]['Synonyms'].values.tolist()
        dfstartsWithList=df[df['Chemicalformula'].str.startswith(input_str)]['Synonyms'].values.tolist()
        if len(dfContainsWithList)>0 and len(dfstartsWithList)>0:
            dfstartsWithList.extend(list(set(dfContainsWithList)-set(dfstartsWithList)))
            return dfstartsWithList
        elif len(dfContainsWithList)>0 and len(dfstartsWithList)==0:
            return dfContainsWithList
        else:
            return None 


'''
Function to search by CAS NUMBER
'''
def search_by_cas_number(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['CAS_Number'].str.contains(input_str)]
        if len(df)>0:
            return df.values.tolist()
        else:
            return None 


'''
Function to search by Synonyms
'''
def search_by_synonyms(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Synonyms'].str.contains(input_str)]
        if len(df)>0:
            return df.values.tolist()
        else:
            return None 


'''
Function to search by Chemicalformula
'''
def search_by_chemicalformula(input_str):
        stream = pkg_resources.resource_stream(__name__, 'data/cas_rn_dataset.csv')
        df=pd.read_csv(stream,encoding='cp1252')
        df=df[df['Chemicalformula'].str.contains(input_str)]
        if len(df)>0:
            return df.values.tolist()
        else:
            return None 
