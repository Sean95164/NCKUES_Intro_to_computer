students = [[] for i in range(3)]
for id,student in enumerate("ABC"):
    students[id].append(student)
    print(f"輸入學生{student}成績")
    
    Sum = 0
    for subject in ["國文","數學","英文"]:
        
        score = int(input(f"{subject}:"))
        print(f"{subject}:{score}")
        students[id].append(score)
        
        Sum+=score
    students[id].append(round(Sum/3,1))
    
for i in range(3):
    print(students[i])
    
    
        