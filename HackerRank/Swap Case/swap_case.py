def swap_case(s):
    swap=""
    for i in s:
        if (i.isupper() == False):
            upper = i.upper()
            swap+=upper
        else:
            lower = i.lower()
            swap+=lower
    #print(swap)
        
    return(swap)
