#!/usr/bin/env python
import sys

flagged_company_dict={}
#Iterating over the inputs provided by mapper
for line in sys.stdin:
    line = line.strip()
    #Splitting the input based on delimiter
    companyName, count = line.split('\t', 1)
    #Doing the count for each company occurance
    if companyName in flagged_company_dict:
            newCount=flagged_company_dict.get(companyName)+1
            flagged_company_dict.update({companyName:newCount}) 
    else:
            flagged_company_dict.update({companyName:1})
#Sorting and printing the output        
for key,value in sorted(flagged_company_dict.items()):
    print '%s\t%s' %(key,value)
