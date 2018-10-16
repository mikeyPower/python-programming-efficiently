'''
Question:
1. Find the five athletes who won the most gold medals?

2. Find the five athletes who won gold medals in the largest number of different events?
'''


# Takes a list and removes 'men' and 'women' to clean the data and joins the
# elements in the list to form a string sperated by a space
def clean(event):
    #print(event)
    if "men" in event:
        event.remove("men")
    elif "women" in event:
        event.remove("women")

    return ' '.join(event)





# Open gold medal text file
goldmedals = open("goldmedals.txt","r")

# initalize gold medal dictionary and medal count 
gold_medal_dictionary = {}
different_event_dictionary ={}
medal_count = 0
different_event = 0

# Loop through each line of the gold medals txt file
for line in goldmedals:
   # print(line[1])
    array = line.rstrip().split('\t') # split the line into an array delimited by a tab
    #print(array)
    name = array[1] 
    all_event = array[3]
    event = clean(all_event.split())
    print(event)
   
   # if the name is all ready in the dictionary get the current
   # medal count and add 1 to it
   # else create a new key with the name and value of 1, since it's the
   # first time we've seen the name
    if name in gold_medal_dictionary:
        medal_count = gold_medal_dictionary[name]
        medal_count = medal_count +1
        gold_medal_dictionary[name]=medal_count
    else:
        gold_medal_dictionary[name] = 1



    if name in different_event_dictionary and event not in different_event_dictionary[name]:
       different_event_dictionary[name].append(event)
      # print(name, different_event_dictionary[name])
    else:
        different_event_dictionary[name] = [event]

# loop through 5 times in order to fnd the top 5 medalist
medal_count =0
no_of_events =0
print("five athletes who won the most gold medals:")
for i in range(5):

    # find the largest medal count and print the name belonging to it
    for key,val in gold_medal_dictionary.items():
        if val > medal_count:
            name = key
            medal_count = val
    print(name, medal_count)
    medal_count =0
     # pop that name so it doesn't keep appearing
    gold_medal_dictionary.pop(name, None)


print("\nfive athletes who won gold medals in the largest number of different events:")
# Similar to above only we are trying to find the most gold medals in different events
for i in range(5):
    for key,val in different_event_dictionary.items():
       
        if len(val) > no_of_events:
          
            name = key
            no_of_events = len(val)
    print(name, no_of_events)
    no_of_events =0
    # pop that name so it doesn't keep appearing
    different_event_dictionary.pop(name, None)



