'''
You have a record of N students. Each record contains the student's name, 
and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. 
The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type. 
The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.
'''

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    total = 0;
    for i in student_marks[query_name]:
        total = total + i;

    average = total / len(student_marks[query_name])

    print("%.2f" %average)
