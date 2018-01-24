#!/usr/bin/env python
import sys

flaggedCompany=[]
doNotCallNumbers = ["2166849356","4049345110","5893715037","9457920329"]
list_of_line=[]
#Iterating over input lines
for line in sys.stdin:
    list_of_line.append(line)
    line = line.strip()
    #Splitting each line on the basis of delimiter
    words = line.split(";")
    #Preparing the flagged company list
    if (words[3].strip() in doNotCallNumbers):
        flaggedCompany.append(words[1]) 
    

flaggedCompany=list(set(flaggedCompany))   

#If company is a flaggedcompany, print the output
for item in list_of_line:
    list_line = item.strip()
    list_words = item.split(";")
    if list_words[1] in flaggedCompany:
        print '%s\t%s' %(list_words[3],"Flagged")
