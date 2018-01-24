#!/usr/bin/env python
import sys
companyList=[]
recipient_list=[]
recipientDictionary={}
maximumRecipient=[]
#Iterating over the inputs provided by mapper
for line in sys.stdin:
    line = line.strip()
    #Splitting the input based on delimiter
    obtainedValues = line.split('\t')
    recipient=""
    flag=""
    recipient_list.append(obtainedValues[0])
#Iterating over each input to update recipient count in dictionary
for item in recipient_list:
    recipient=item
    if recipient in recipientDictionary:
            newCount=recipientDictionary.get(recipient)+1
            recipientDictionary.update({recipient:newCount}) 
    else:
            recipientDictionary.update({recipient:1})
    
for item in recipientDictionary:
    maximumRecipient.append(recipientDictionary.get(item))
#Populating the maximum count table with top 3 values
maximumRecipient=list(set(maximumRecipient))
newList=sorted(maximumRecipient, reverse=True)[:3]

#Printing the output for the top-3 values
for count in newList:
    for item in recipientDictionary:
        if recipientDictionary.get(item)==count:
            mobile_number=item
            mobile_number=mobile_number[:6] + '-' + mobile_number[6:]
            mobile_number=mobile_number[:3] + ' ' + mobile_number[3:]
            mobile_number=mobile_number[:0] + '(' + mobile_number[0:]
            mobile_number=mobile_number[:4] + ')' + mobile_number[4:]
            print '%s\t%s' %(mobile_number,count)
