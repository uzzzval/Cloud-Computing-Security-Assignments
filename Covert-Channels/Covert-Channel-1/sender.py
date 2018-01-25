#!/usr/bin/env python

import os
import time
import random
import math
import mmap

pth = os.path.dirname(os.path.abspath(__file__))
in_file = open(pth + "/file.txt", 'r+')
in_file_map = mmap.mmap(in_file.fileno(), 0)

def transmit_one():
        chars_in_file = 150612736 

	start_time = time.time()
     	for i in range (0, 5):
        	x = random.randint(0, int((2.0/10)*chars_in_file))
   		y = random.randint(int((8.0/10)*chars_in_file), chars_in_file)
		in_file_map[x:y]
	end_time = time.time()
        transmit_time = round(end_time - start_time, 3)
        print "Time to transmit '1' bit is " + str(transmit_time) + " seconds"

def send_message(bit_stream):
	start_time = time.time()
	for i in range(0,len(bit_stream)):
       		if bit_stream[i] == '1':
               		 transmit_one()
        	else:
                	time.sleep(1.0)
	
message = raw_input("\nWhat message (1's and 0's) do you want to send?: ")
message = list("1" + message + "1")   

send_message(message)
in_file.close()
