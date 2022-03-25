'''
Read an integer N.

Without using any string methods, try to print the following:

123...N

Note that "..." represents the values in between.
'''



from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

    #accum =1
    #total =0
    #for i in range(n+1):
      #  total = 10 * total
        #accum = accum *10
       # total = total + i
        
    #print(total)
    print(*range(1, n+1), sep='')   
