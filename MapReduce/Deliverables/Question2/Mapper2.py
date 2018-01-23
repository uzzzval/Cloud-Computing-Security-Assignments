#!/usr/bin/env python
import sys

flaggedCompany=[]
doNotCallNumbers = ["2166849356","4049345110","5893715037","9457920329"]
companyCount={}
#Iterating over each line
for line in sys.stdin:
    line = line.strip()
    #Splitting each line on the basis of delimiter
    words = line.split(";")
    #Adding the count of each company to dictionary
    if words[1] in companyCount:
        newCount=companyCount.get(words[1])+1
        companyCount.update({words[1]:newCount}) 
    else:
        companyCount.update({words[1]:1})
    #Storing the flagged companies   
    if (words[3].strip() in doNotCallNumbers):
        flaggedCompany.append(words[1])

#Printing the output      
flaggedCompany=list(set(flaggedCompany))
print '%s\t%s' %(flaggedCompany,companyCount)
