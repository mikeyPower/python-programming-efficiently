name_to_grade=[]
n = 0
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    name_to_grade.append([name,score])
    n = n +1

#sort list
#print(name_to_grade)
for i in range(n):
   # m = name_to_grade[i]
    for j in range(n):
        m = name_to_grade[i]
        k = name_to_grade[j]
        if k[1] < m[1] and j >= i:
            tmp = m
            name_to_grade[i]=k
            name_to_grade[j]=tmp

#print(name_to_grade)

for i in range(n):
    lowest = name_to_grade[0]
    second = name_to_grade[i]
    if second[1] > lowest[1]:
        sec_grade=second[1]
        name_to_grade.pop(i)
        break
        

#create new list of second lowest score

second_grade_list = [second[0]]

#check duplicate scores

for i in name_to_grade:

    if sec_grade == i[1] :
        second_grade_list.append(i[0])


#sort alphabet
n = len(second_grade_list)
for i in range(n):
    
    for j in range(n):
        k = second_grade_list[j]
        m = second_grade_list[i]
        if k < m and j > i:
            tmp = m
            second_grade_list[i]=k
            second_grade_list[j]=tmp

#print answer
for i in second_grade_list:
    print(i)
