# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:11:23 2021

@author: 91965
"""


========================WHILE LOOPS=======================================



a=[1,2,3,4,5]    
while a:
    print(a.pop())


SINGLE STATEMENT WHILE LOOP:

count=0
while(count<4): count+=1; print("Hi:",count)  


LOOP CONTROL STATEMENTS

1. CONTINUE STATEMENT: It returns the control to the beginning of thr loop  


i=0
a="presentation"

while i <len(a):
    if a[i]=="i" or a[i]=="e":
        i+=1
        continue
    print("Current letter is: ", a[i])
    i+=1
    
    

2. BREAK STATEMENT: It brings control out of the loop

i=0
a="presentation"

while i <len(a):
    if a[i]=="i" or a[i]=="e":
        i+=1
        break
    print("Current letter is: ", a[i])
    i+=1

3. PASS STATEMENT: We use pass statement to write empty loops. 

i=0
a="presentation"
while i <len(a):
    i+=1
    pass
print("the length of a is: ", i)
    


i=0
a="presentation"
while i <len(a):i+=1; pass
print("value is ", i)


WHILE-ELSE LOOP

In this else clause is only executed when your while condition becomes false. If we break out of the 
loop or if an exception is raised, it won't'  be executed. 



i=0
while i<4:
    i+=1
    print(i)
else:
    print("no break")
    
i=0
while i<4:
    i+=1
    print(i)
    break
else:
    print("no break")
    