#!/usr/bin/env python
import sys
companyList=[]
caller_list=[]
callerDictionary={}
maximumRecipient=[]
#Iterating over the inputs provided by mapper
for line in sys.stdin:
    line = line.strip()
    #Splitting the input based on delimiter
    obtainedValues = line.split('\t')
    caller=""
    flag=""
    caller_list.append(obtainedValues[0])

#Storing the calling count of each number in dictionary  
for item in caller_list:
    caller=item
    if caller in callerDictionary:
        newCount=callerDictionary.get(caller)+1
        callerDictionary.update({caller:newCount}) 
    else:
        callerDictionary.update({caller:1})
        
       
for item in callerDictionary:
    maximumRecipient.append(callerDictionary.get(item))
#Populating the maximum list and sorting
maximumCaller=list(set(maximumRecipient))
newList=sorted(maximumCaller, reverse=True)[:3]

#Printing the output for top 2 values
for count in newList:
    for item in callerDictionary:
        if callerDictionary.get(item)==count:
            mobile_number=item
            mobile_number=mobile_number[:6] + '-' + mobile_number[6:]
            mobile_number=mobile_number[:3] + ' ' + mobile_number[3:]
            mobile_number=mobile_number[:0] + '(' + mobile_number[0:]
            mobile_number=mobile_number[:4] + ')' + mobile_number[4:]
            print '%s\t%s' %(mobile_number,count)
 

    
    
