#!/usr/bin/env python
import sys
companyList=[]
companyDict=[]
#Iterating over the inputs provided by mapper
for line in sys.stdin:
    line = line.strip()
    #Splitting the input based on delimiter
    companyNameList, finalCountDict = line.split('\t', 1)
    #String Manipulation
    companyNameList=companyNameList.replace("[","")
    companyNameList=companyNameList.replace("]","")
    companyNameList=companyNameList.replace(" '","")
    companyNameList=companyNameList.replace("'","")
    companyList=companyNameList.strip().split(",")
  
    finalCountDict=finalCountDict.replace("{","")
    finalCountDict=finalCountDict.replace("}","")
    finalCountDict=finalCountDict.replace("'","")
    finalCountDict=finalCountDict.replace(", ",",")
    finalCountDict=finalCountDict.replace(": ",":")
    companyDict=finalCountDict.split(",");
    companyList.sort()
    
    #Iterating over each item and printing the output
    for listItem in companyList:
        for dictItem in companyDict:
            if listItem in dictItem:
                print dictItem.replace(":","\t")
