import pandas as pd
import importlib_resources
import cas_rn_validator.validator as v
import os
'''
Function to search ChemicalFormula With CAS NUMBER
'''
def getChemicalFormulaWithCAS(input_str):
    # validate cas registry number
    if v.validateCAS_RN(input_str)==True:
        # exception handling for wrong cas_rn dataset file format
        try:
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase# 
                    input_str_lower = input_str.lower()  
                    # Filter the DataFrame based on the lowercase 'Synonyms'
                    df_filtered = df[df['Synonyms'].str.lower()  == input_str_lower] 
                    # Retrieve the chemical formula from the filtered DataFrame
                    CAS_Number = df_filtered['CAS_Number'].tolist()[0] if not df_filtered.empty else None 
                    return CAS_Number
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    # Filter the DataFrame based on the lowercase 'Synonyms'
                    df_filtered = df[df['Synonyms'].str.lower()  == input_str_lower] 
                    # Retrieve the chemical formula from the filtered DataFrame
                    Chemicalformula = df_filtered['Chemicalformula'].tolist()[0] if not df_filtered.empty else None 
                    return Chemicalformula 
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    # Filter the DataFrame based on the lowercase 'Chemicalformula'
                    df_filtered = df[df['Chemicalformula'].str.lower()  == input_str_lower] 
                    # Retrieve the chemical formula from the filtered DataFrame
                    Chemicalformula = df_filtered['CAS_Number'].tolist()[0] if not df_filtered.empty else None 
                    return Chemicalformula
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    # Filter the DataFrame based on the lowercase 'Chemicalformula'
                    df_filtered = df[df['Chemicalformula'].str.lower()  == input_str_lower] 
                    # Retrieve the chemical formula from the filtered DataFrame
                    Synonyms = df_filtered['Synonyms'].tolist()[0] if not df_filtered.empty else None 
                    return Synonyms
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['CAS_Number'].str.lower().str.contains(input_str_lower,regex=False)]['Chemicalformula'].values.tolist()
                    dfstartsWithList=df[df['CAS_Number'].str.lower().str.startswith(input_str_lower)]['Chemicalformula'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['CAS_Number'].str.lower().str.contains(input_str_lower,regex=False)]['Synonyms'].values.tolist()
                    dfstartsWithList=df[df['CAS_Number'].str.lower().str.startswith(input_str_lower)]['Synonyms'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['Synonyms'].str.lower().str.contains(input_str_lower,regex=False)]['CAS_Number'].values.tolist()
                    dfstartsWithList=df[df['Synonyms'].str.lower().str.startswith(input_str_lower)]['CAS_Number'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['Synonyms'].str.lower().str.contains(input_str_lower,regex=False)]['Chemicalformula'].values.tolist()
                    dfstartsWithList=df[df['Synonyms'].str.lower().str.startswith(input_str_lower)]['Chemicalformula'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['Chemicalformula'].str.lower().str.contains(input_str_lower,regex=False)]['CAS_Number'].values.tolist()
                    dfstartsWithList=df[df['Chemicalformula'].str.lower().str.startswith(input_str_lower)]['CAS_Number'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    dfContainsWithList=df[df['Chemicalformula'].str.lower().str.contains(input_str_lower,regex=False)]['Synonyms'].values.tolist()
                    dfstartsWithList=df[df['Chemicalformula'].str.lower().str.startswith(input_str_lower)]['Synonyms'].values.tolist()
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    df=df[df['CAS_Number'].str.lower().str.contains(input_str_lower,regex=False)]
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    df=df[df['Synonyms'].str.lower().str.contains(input_str_lower,regex=False)]
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
            for entry in importlib_resources.files('cas_rn_validator.data').iterdir():
                if((entry.name.split('.')[-1])=='csv'):
                    # reading file path
                    dataset_path = os.path.join(os.path.dirname(__file__), 'data',entry.name )
                    # reading csv and getting data
                    df=pd.read_csv(dataset_path)
                    # Convert input string to lowercase
                    input_str_lower = input_str.lower()  
                    df=df[df['Chemicalformula'].str.lower().str.contains(input_str_lower,regex=False)]
                    if len(df)>0:
                        return df.values.tolist()
                    else:
                        return None 
                else:
                    raise Exception('Please put data file in csv format')
        except Exception as E:
            return(E)

