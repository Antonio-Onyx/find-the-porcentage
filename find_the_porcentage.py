

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #print(student_marks)
    
    
    for key in student_marks.items():
        if key[0] == query_name:
            porcentage = sum(key[1]) / len(key[1])
            print("{0:.2f}".format(porcentage))
            