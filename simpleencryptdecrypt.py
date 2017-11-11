#!/usr/bin/python

#define encoding function
def encode(f):
    list2 = ["b", "c", "d", "e"]
    for n in f:
        if n > 0:
           f.append(list2)
           print (list2)
           return()
           
#create empty list
list = []


#enter number to be encoded one by one
print ("enter number digit by digit, press enter after each digit")
#put the numbers into a list
for f in xrange(4):
    digit = raw_input()
    list.append(digit)
    print (list[0], "ignore")
    
#start encode
print ("confirm encrypt? if so type 1")
a = raw_input()
if a == 1:
      print ("ok")
encode(list)   


print ("decrypt? yes or no")
b = raw_input()
if b == "yes":
   print (list, "original data, encrypted data", "end of demo")

if b == "no":
   print ("ok, but your data wont be saved, please await future versions!")

    