'''
Created on 1 jan. 2017

@author: Adrian
'''
from datetime import datetime

def listSum(NumberList):
    '''
    Adds numbers in a list.
    '''
    total = 0
    for number in NumberList:
        total += number
        
    return total

