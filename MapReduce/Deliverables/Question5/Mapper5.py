#!/usr/bin/env python
import sys

doNotCallNumbers = ["2166849356","4049345110","5893715037","9457920329"]
flaggedCompanies=[]
line_list=[]
#Iterating over each input line
for line in sys.stdin:
    line_list.append(line)
    line = line.strip()
    #Splitting each line on the basis of delimiter.
    words = line.split(";")
    #Preparing the flagged company list
    if words[3].strip() in doNotCallNumbers:
        flaggedCompanies.append(words[1])

flaggedCompanies=list(set(flaggedCompanies))

#printing the timestamp as the output
for line_in_line_list in line_list:
    line_in_line_list = line_in_line_list.strip()
    words_in_line_list = line_in_line_list.split(";")
    print '%s\t%s' %(words_in_line_list[0],1)
