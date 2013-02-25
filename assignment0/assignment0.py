#!/usr/bin/python
# Add your code here
print("I love the Crimson tech department!")

###### 2. FIZZBUZZ #######
def fizz_buzz():
	for x in range(100):
		if (x+1) % 15 == 0:
			print("FizzBuzz")
		elif (x+1) % 3 == 0:
			print("Fizz")
		elif (x+1) % 5 == 0:
			print("Buzz")
		else: print x+1
#fizz_buzz()

###### 3. Letter Swap #######
import collections
import re
import sys
def letterswap(s):
	# get rid of all non alphanumeric characters
	r = re.sub(r'\W+', '', s)
	# puts into a sorted array each letter and the number of times it appears
	r = collections.Counter(r).most_common()
	for c in s:
		if c == r[0][0]:
			c = r[-1][0]
			sys.stdout.write(c)
		elif c == r[-1][0]:
			c = r[0][0]
			sys.stdout.write(c)
		else: sys.stdout.write(c)
	print("")
letterswap("The quick brown fox jumped over the lazy dog")

###### 4. Sort Concat #######
def sortcat(n, *strg):
    # sort the strings, shortest to longest
	stringer = sorted(strg, key=len)
	concat = ""
	if n == -1: #not elegent, but take care of the -1 case for n
		n = len(strg)
    #concat the strings
	for x in range(n):
		concat = concat + stringer[-x-1]
	print concat
sortcat(-1, "hello" , "sir", "world")

###### 5. Look Away #######
import random
def look(trials):
	won = 0.0
    # loop the number of trials
	for x in range(trials):
		Mario = Wario = Peach = 0
        # loop 5 times
		for y in range(5):
            # if the random value is less than or equal to 1 from [0,5] set the value to 1
			if random.random()*5 <=1:
				Mario = 1
			if random.random()*5 <=1:
				Wario = 1
			if random.random()*5 <=1:
				Peach = 1
		if Mario == 1 and Wario == 1 and Peach == 1:
			won = won+1
	print won/trials 
look(10000)
# exact should be (1-(4/5)^5)^3

####### 8. Shuttleboy #######
import urllib, json, time
from datetime import datetime, date, timedelta
def shuttle():
    # get the JSON data
    response = urllib.urlopen("http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass%20Ave%20Garden%20St&output=json")
    content = response.read()
    data = json.loads(content)
    # get the times for the shuttles
    t1 = datetime.strptime(str(str(data[0]).split("'")[3]).split("T")[1]+".0", '%H:%M:%S.%f')
    t2 = datetime.strptime(str(str(data[1]).split("'")[3]).split("T")[1]+".0", '%H:%M:%S.%f')
    t3 = datetime.strptime(str(str(data[2]).split("'")[3]).split("T")[1]+".0", '%H:%M:%S.%f')
    # get the current time
    now = datetime.strptime(str(datetime.time(datetime.now())), '%H:%M:%S.%f')
    print "The next shuttle departs in " + str(str(t1-now).split(":")[0]) + " hours and " + str(str(t1-now).split(":")[1]) + " minutes from now " + "at " + str(str(t1).split("01")[2])
    print "After that, the next shuttle departs in " + str(str(t2-now).split(":")[0]) + " hours and " + str(str(t2-now).split(":")[1]) + " minutes from now " + "at " + str(str(t2).split("01")[2])
    print "After that, the next shuttle departs in " + str(str(t3-now).split(":")[0]) + " hours and " + str(str(t3-now).split(":")[1]) + " minutes from now " + "at " + str(str(t3).split("01")[2])
shuttle()