#You are given the firstname and lastname of a person on two different lines. 
#Your task is to read them and print the following:

#Hello firstname lastname! You just delved into python.

def print_full_name(a, b):
    print "Hello "+a+" "+b+"! You just delved into python."

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)