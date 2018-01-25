#!/usr/bin/env python
'''
    File name: receiver.py
    Authors: Joshua Ciocco, Sean Futch, Ujjawal Sharma 
    Date created: 10/12/2017 
    Date last modified: 10/20/2017 
    Python Version: 2.7.12
'''
import os
import math
import numpy
import time
import random
import mmap

path = os.path.dirname(os.path.abspath(__file__))

in_file = open(path + "/file.txt", 'r+')
chars_in_file = 210612736            
x = int((0.2) * chars_in_file)      #{x, y} represent fixed locations in file
y = int((0.8) * chars_in_file)

file_map = mmap.mmap(in_file.fileno(), 0)

def turn_on(read_times):
        noise_correction = 3 
	ra = list()
	for i in range(0, read_times):
        	start_time = time.time()
		for i in range(0, noise_correction):
			file_map[x:y]
		end_time = time.time()
                elapsed_time = round(end_time - start_time, 3)
		ra.append(elapsed_time)
		#print elapsed_time
        ra = ra[1:]              # throw out first value
	return(ra)

def id_ones(ra):
	str = list()
	i = 0
	while i < len(ra):
		count = 0
		j = i
                
		while round(ra[j], 2) >= threshold : 
			if (j + 1) == len(ra):
				break
			else:
				j +=  1
			count += 1
		if count >= 10 :		
			str.append(i)
		 	str.append(j)
                        #print "str is:", str
			i = j
		else:
			i +=  1
	return str

def received_message(time_ra):
	ones_ra = list()
	zeroes_ra = list()
	for i in range(0, len(time_ra)-1, 2):
		ones_ra.append(time_ra[i+1]-time_ra[i])
	for i in range(1, len(time_ra)-1, 2):
		zeroes_ra.append(time_ra[i+1]-time_ra[i])
	for i in range(0, len(ones_ra)):
		ones_ra[i] = int(round(ones_ra[i]/read_one))
	for i in range(0, len(zeroes_ra)):
		zeroes_ra[i] = int(round(zeroes_ra[i]/read_zero))

	msg = list()
	i = j = k = 0

	while k < len(ones_ra) + len(zeroes_ra):
		if k%2 == 1:
			msg.append(zeroes_ra[j])
			j += 1
                else:
			msg.append(ones_ra[i])
			i += 1
		k += 1
	message = list()
	for k in range(0, len(msg)):
		if k%2 == 1:
			for i in range(0, msg[k]):
				message.append('0')
		else:
			for j in range(0, msg[k]):
				message.append('1')
        #print str(message[1:-1])
	ans =''.join(message[1:-1]) 
	#for i in range(0,len(message)):
	#	ans = ans + str(message[i])

	return ans

# Calibration conducts statistical analysis on a test run 
print "Calibrating average latency and threshold..."
calibration_ra = turn_on(50)

mean_latency = numpy.mean(calibration_ra, axis=0)          
print "Mean latency time (seconds) is: ", round(mean_latency, 3) 

std_dev = numpy.std(calibration_ra, axis=0)  
print "Standard deviation (seconds) is: ", round(std_dev, 3)

threshold = mean_latency + std_dev
print "The threshold (mean + standard deviation) is: ", round(threshold, 3)

n = input("How long (seconds) do you want the program to listen for bits\n")
seconds = int(n/mean_latency)
 
times_ra = turn_on(seconds)
read_one = 2.0/mean_latency        #observed from sender.py
read_zero = 1.0/mean_latency       #sender.py sleeps 1 second to send '0' bit

indexes = id_ones(times_ra)

bit_stream = received_message(indexes)

print "The bits transmitted by sender is: ", bit_stream 

in_file.close()
