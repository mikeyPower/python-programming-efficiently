#You are given the year, and you have to write a function to check if the year is leap or not

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year in range(1900,pow(10,5)+1): 
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
    
    return leap
