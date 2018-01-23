#!/usr/bin/env python
import sys

doNotCallNumbers = ["2166849356","4049345110","5893715037","9457920329"]
#Iterating over each line
for line in sys.stdin:
    line = line.strip()
    #Splitting each line on the basis of delimiter.
    words = line.split(";")
    #Printing the output
    if words[3].strip() in doNotCallNumbers:
        print '%s\t\t%s' % (words[1],1)
