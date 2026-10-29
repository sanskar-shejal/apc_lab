def exam_details():
    semesters = int(input("enter number of semesters: "))
    marks_list = []
    total = 0
    for i in range(1,semesters+1):
        marks = float(input("enter marks of semester "+str(i)+": "))
        marks_list.append(marks)
        total += marks
    average = total / semesters
    print()
    print("SEMESTER MARKS")
    for i in range(semesters):
        print("semester",i+1,"=",marks_list[i])
    print()
    print("total =",total)
    print("average =",average)
    if average >= 40:
        print("result = PASS")
    else:
        print("result = FAIL")
