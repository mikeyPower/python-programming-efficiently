#!/bin/python

'''
Enter your code here. Read input from STDIN. Print output to STDOUT

Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''

N = int(raw_input())

if N%2 != 0 or (N%2 ==0 and (N >=6 and N <= 20)):
    print("Weird")
    
elif N%2 == 0 and ((N >= 2 and N<= 5) or (N > 20)):
    print("Not Weird")
    
