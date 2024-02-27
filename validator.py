import pandas as pd


'''
Function to validate the CAS REGISTRY NUMBER
'''
def validateCAS_RN(input_str):
    lst=input_str.split('-')
    if len(lst)==3 and (lst[0].isdigit() and len(lst[0])>=2 and len(lst[0])<=7) and  (lst[1].isdigit() and len(lst[1])==2) and (lst[2].isdigit() and len(lst[2])==1):
            if str(sum([(i+1)*int(j) for i,j in enumerate(''.join([i[::-1] for i in lst][1::-1]))])%10) ==str(lst[2]):
                flag=True
            else:
                flag=False
    else:
            flag=False
    return flag


'''
Function to validate the CAS REGISTRY NUMBER with Message
'''
def validateCASwithMessage(input_str):
    if validateCAS_RN(input_str)==True:
        return('CAS Registry Number is valid')
    else:
        return('CAS Registry Number is invalid')

