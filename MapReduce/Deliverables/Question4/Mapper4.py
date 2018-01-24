#!/usr/bin/env python
import sys

doNotCallNumbers = ["2166849356","4049345110","5893715037","9457920329"]
flaggedCompanies=[]
line_list=[]

#Iterating over the inputs
for line in sys.stdin:
    line_list.append(line)
    line = line.strip()
    #Splitting each word on the basis of delimiter
    words = line.split(";")
    #Preparing list of flagged companies
    if words[3].strip() in doNotCallNumbers:
        flaggedCompanies.append(words[1])

#If Company name is flagged, print the caller
for line_from_list in line_list:
    line_from_list = line_from_list.strip()
    words_of_line_from_list = line_from_list.split(";")
    if words_of_line_from_list[1] in flaggedCompanies:
        print '%s\t%s' %(words_of_line_from_list[2],1)
