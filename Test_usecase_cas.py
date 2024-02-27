import pandas as pd
import validator as v
import search as s
input_str=input("enter value: ")
# print(v.validateCAS_RN(input_str))
# print(v.validateCASwithMessage(input_str))
# print(s.getChemicalFormulaWithCAS(input_str))
# print(s.getSynonymsWithCAS(input_str))
# print(s.getChemicalFormulaWithSynonyms(input_str))
# print(s.getCASNumberWithSynonyms(input_str))
# print(s.getCASNumberWithChemicalFormula(input_str))
# print(s.getSynonymsWithChemicalFormula(input_str))


# print(s.search_by_cas_number(input_str))
# print(s.search_by_synonyms(input_str))
print(s.search_by_chemicalformula(input_str))

# print(s.searchChemicalFormulaWithCAS(input_str))
# print(s.searchSynonymsWithCAS(input_str))
# print(s.searchCASNumberWithSynonyms(input_str))
# print(s.searchChemicalFormulaWithSynonyms(input_str))
# print(s.searchCASNumberWithChemicalFormula(input_str))
# print(s.searchSynonymsWithChemicalFormula(input_str))
