#!/usr/bin/env python
import sys

hour_dictionary={}
hour_list=[]
count_list=[]
#Iterating over the inputs provided by mapper
for line in sys.stdin:
    line = line.strip()
    #Splitting the input based on delimiter
    obtainedTimeString = line.split('\t')
    caller=""
    flag=""
    onlyTime=obtainedTimeString[0].split(" ")
    hour_value=onlyTime[1].split(":")
    hour_list.append(hour_value[0])

#Storing the count of each hour in the dictionary   
for item in  hour_list:
    if item in hour_dictionary:
        newCount=hour_dictionary.get(item)+1
        hour_dictionary.update({item:newCount}) 
    else:
        hour_dictionary.update({item:1}) 

for item in hour_dictionary:
    count_list.append(hour_dictionary.get(item))

maximum_list=sorted(count_list, reverse=True)[:3]

#getting the maximum 3 top values
reverse_sorted_list=[]
while maximum_list:
    maximum = maximum_list[0]  # arbitrary number in list 
    for x in maximum_list: 
        if x > maximum:
            maximum = x
    reverse_sorted_list.append(maximum)
    maximum_list.remove(maximum) 

#Printing the top 3 values in the required way
for reverse_item in reverse_sorted_list:
    for item in hour_dictionary:
        if hour_dictionary.get(item) == reverse_item:
            time=int(item)
            suffix=""
            if time<12:
                suffix=" am"
            if time==12:
                suffix=" noon"
            if time>12:
                time=time-12
                suffix=" pm"
            time_value=str(time)+suffix   
            print '%s\t%s' %(time_value,hour_dictionary.get(item))
