# 1. Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.

# name = input("enter student name: ")
# roll = input("enter roll number: ")
# branch = input("enter branch: ")
# semester = input("enter semester: ")

# file = open("student.txt","w")

# file.write("name = " + name + "\n")
# file.write("roll number = " + roll + "\n")
# file.write("branch = " + branch + "\n")
# file.write("semester = " + semester + "\n")

# file.close()

# print("file created")


# 2. Write a program to open a text file and display its complete contents.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# print(s)


# 3. Write a program to append additional student information to an existing file without deleting its previous contents.

# filename = input("enter file name: ")

# name = input("enter student name: ")
# roll = input("enter roll number: ")
# branch = input("enter branch: ")
# semester = input("enter semester: ")

# file = open(filename,"a")

# file.write("\nname = " + name)
# file.write("\nroll number = " + roll)
# file.write("\nbranch = " + branch)
# file.write("\nsemester = " + semester)

# file.close()

# print("information added")


# 4. Write a program to read a text file line by line and display each line separately.

# filename = input("enter file name: ")

# file = open(filename,"r")

# for line in file:
#     print(line,end="")

# file.close()


# 5. Write a program to count and display the total number of lines present in a text file.

# filename = input("enter file name: ")

# file = open(filename,"r")
# lines = file.readlines()
# file.close()

# print("total lines =",len(lines))


# 6. Write a program to count the total number of words present in a text file.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# words = s.split()

# print("total words =",len(words))


# 7. Write a program to count the total number of characters in a text file, including spaces.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# print("total characters =",len(s))


# 8. Write a program to read a text file and display its lines in reverse order.

# filename = input("enter file name: ")

# file = open(filename,"r")
# lines = file.readlines()
# file.close()

# for i in reversed(lines):
#     print(i,end="")


# 9. Read a text file and count the number of vowels and consonants present in the file.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# vowels = 0
# consonants = 0

# for i in s:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("vowels =",vowels)
# print("consonants =",consonants)


# 10. Read a text file and calculate the number of alphabets, digits, spaces, and special characters.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# alphabets = 0
# digits = 0
# spaces = 0
# special = 0

# for i in s:
#     if i.isalpha():
#         alphabets += 1
#     elif i.isdigit():
#         digits += 1
#     elif i.isspace():
#         spaces += 1
#     else:
#         special += 1

# print("alphabets =",alphabets)
# print("digits =",digits)
# print("spaces =",spaces)
# print("special characters =",special)


# 11. Read a text file and find the longest word present in the file.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# words = s.split()

# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("longest word =",longest)


# 12. Read a text file and count how many times each word occurs. Display the result using a dictionary.

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# words = s.split()

# frequency = {}

# for i in words:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1

# print(frequency)


# 13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.

# filename = input("enter file name: ")
# word = input("enter word to search: ")

# file = open(filename,"r")
# lines = file.readlines()
# file.close()

# count = 0
# line_numbers = []

# for i in range(len(lines)):
#     words = lines[i].split()
    
#     for j in words:
#         if j == word:
#             count += 1
            
#             if i+1 not in line_numbers:
#                 line_numbers.append(i+1)

# print("occurrences =",count)
# print("line numbers =",line_numbers)


# 14. Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.

# filename = input("enter file name: ")
# old = input("enter word to replace: ")
# new = input("enter new word: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# s = s.replace(old,new)

# newfile = input("enter new file name: ")

# file = open(newfile,"w")
# file.write(s)
# file.close()

# print("file saved")


# 15. Read a Python source file and create another file after removing single-line comments.

# filename = input("enter python file name: ")
# newfile = input("enter new file name: ")

# file = open(filename,"r")
# lines = file.readlines()
# file.close()

# file = open(newfile,"w")

# for line in lines:
#     if "#" in line:
#         line = line[:line.index("#")]
    
#     if line.strip() != "":
#         file.write(line)

# file.close()

# print("file created")


# 16. Read a text file and create another file containing the same text in uppercase.

# filename = input("enter file name: ")
# newfile = input("enter new file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# s = s.upper()

# file = open(newfile,"w")
# file.write(s)
# file.close()

# print("file created")


# 17. Create a file containing student records in the format: RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to display all records, find the student with highest marks, calculate average marks, and display students who scored more than 80.

# file = open("students.txt","r")
# lines = file.readlines()
# file.close()

# highest_name = ""
# highest_marks = 0
# total = 0
# count = 0

# print("all records:")

# for line in lines:
#     data = line.strip().split(",")
    
#     roll = data[0]
#     name = data[1]
#     marks = int(data[2])
    
#     print(roll,name,marks)
    
#     total += marks
#     count += 1
    
#     if marks > highest_marks:
#         highest_marks = marks
#         highest_name = name

# print("highest marks =",highest_name,highest_marks)
# print("average marks =",total/count)

# print("students above 80:")

# for line in lines:
#     data = line.strip().split(",")
    
#     if int(data[2]) > 80:
#         print(data[1],data[2])


# 18. Store employee ID, name, department, and salary in a file. Write functions to display all employees, find the highest-paid employee, calculate average salary, and display employees earning above a given salary.

# def display():
#     file = open("employees.txt","r")
    
#     for line in file:
#         print(line.strip())
    
#     file.close()


# def highest():
#     file = open("employees.txt","r")
    
#     highest_salary = 0
#     highest_name = ""
    
#     for line in file:
#         data = line.strip().split(",")
#         salary = float(data[3])
        
#         if salary > highest_salary:
#             highest_salary = salary
#             highest_name = data[1]
    
#     file.close()
    
#     print("highest paid employee =",highest_name)
#     print("salary =",highest_salary)


# def average():
#     file = open("employees.txt","r")
    
#     total = 0
#     count = 0
    
#     for line in file:
#         data = line.strip().split(",")
#         total += float(data[3])
#         count += 1
    
#     file.close()
    
#     print("average salary =",total/count)


# def above():
#     amount = float(input("enter salary: "))
    
#     file = open("employees.txt","r")
    
#     for line in file:
#         data = line.strip().split(",")
        
#         if float(data[3]) > amount:
#             print(data[1],data[3])
    
#     file.close()


# display()
# highest()
# average()
# above()


# 19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.

# file = open("attendance.txt","r")
# lines = file.readlines()
# file.close()

# for line in lines:
#     data = line.strip().split(",")
    
#     roll = data[0]
#     name = data[1]
#     attended = int(data[2])
#     total = int(data[3])
    
#     percentage = (attended/total)*100
    
#     print(name,"=",percentage,"%")
    
#     if percentage < 75:
#         print(name,"has attendance below 75%")


# 20. Store deposits and withdrawals in a file. Read the file and calculate total deposits, total withdrawals, final balance, and largest transaction.

# file = open("transactions.txt","r")
# lines = file.readlines()
# file.close()

# deposits = 0
# withdrawals = 0
# largest = 0

# for line in lines:
#     data = line.strip().split(",")
    
#     transaction = data[0]
#     amount = float(data[1])
    
#     if transaction == "deposit":
#         deposits += amount
#     elif transaction == "withdrawal":
#         withdrawals += amount
    
#     if amount > largest:
#         largest = amount

# balance = deposits - withdrawals

# print("total deposits =",deposits)
# print("total withdrawals =",withdrawals)
# print("final balance =",balance)
# print("largest transaction =",largest)


# 21. Maintain book records containing book ID, title, author, and availability status. Implement operations to add a book, search for a book, issue a book, return a book, and display available books.

# def add_book():
#     id = input("enter book id: ")
#     title = input("enter title: ")
#     author = input("enter author: ")
    
#     file = open("books.txt","a")
#     file.write(id + "," + title + "," + author + ",available\n")
#     file.close()
    
#     print("book added")


# def search_book():
#     title = input("enter title: ")
    
#     file = open("books.txt","r")
    
#     found = False
    
#     for line in file:
#         data = line.strip().split(",")
        
#         if data[1].lower() == title.lower():
#             print(line.strip())
#             found = True
    
#     file.close()
    
#     if not found:
#         print("book not found")


# def issue_book():
#     id = input("enter book id: ")
    
#     file = open("books.txt","r")
#     lines = file.readlines()
#     file.close()
    
#     file = open("books.txt","w")
    
#     for line in lines:
#         data = line.strip().split(",")
        
#         if data[0] == id:
#             data[3] = "issued"
#             line = ",".join(data) + "\n"
        
#         file.write(line)
    
#     file.close()
    
#     print("book issued")


# def return_book():
#     id = input("enter book id: ")
    
#     file = open("books.txt","r")
#     lines = file.readlines()
#     file.close()
    
#     file = open("books.txt","w")
    
#     for line in lines:
#         data = line.strip().split(",")
        
#         if data[0] == id:
#             data[3] = "available"
#             line = ",".join(data) + "\n"
        
#         file.write(line)
    
#     file.close()
    
#     print("book returned")


# def available_books():
#     file = open("books.txt","r")
    
#     for line in file:
#         data = line.strip().split(",")
        
#         if data[3] == "available":
#             print(line.strip())
    
#     file.close()


# add_book()
# search_book()
# issue_book()
# return_book()
# available_books()


# 22. Read the contents of two text files and create a third file containing the contents of both files.

# file1 = input("enter first file name: ")
# file2 = input("enter second file name: ")
# file3 = input("enter new file name: ")

# file = open(file1,"r")
# s1 = file.read()
# file.close()

# file = open(file2,"r")
# s2 = file.read()
# file.close()

# file = open(file3,"w")
# file.write(s1)
# file.write("\n")
# file.write(s2)
# file.close()

# print("file created")


# 23. Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.

# file1 = input("enter first file name: ")
# file2 = input("enter second file name: ")

# f1 = open(file1,"r")
# lines1 = f1.readlines()
# f1.close()

# f2 = open(file2,"r")
# lines2 = f2.readlines()
# f2.close()

# same = True

# length = min(len(lines1),len(lines2))

# for i in range(length):
#     if lines1[i] != lines2[i]:
#         print("files are different")
#         print("first different line =",i+1)
#         same = False
#         break

# if same:
#     if len(lines1) == len(lines2):
#         print("files are identical")
#     else:
#         print("files are different")
#         print("first different line =",length+1)


# Problems on module, Package and Directory


# 1. Create a Python module calculator.py containing functions for addition, subtraction, multiplication, and division. Create another program that imports the module and performs calculations based on user input.

# calculator.py

# def addition(a,b):
#     return a+b

# def subtraction(a,b):
#     return a-b

# def multiplication(a,b):
#     return a*b

# def division(a,b):
#     return a/b


# main.py

# import calculator

# a = float(input("enter first number: "))
# b = float(input("enter second number: "))

# print("addition =",calculator.addition(a,b))
# print("subtraction =",calculator.subtraction(a,b))
# print("multiplication =",calculator.multiplication(a,b))
# print("division =",calculator.division(a,b))


# 2. Create a module student.py containing functions to calculate total marks, percentage, and grade. Import the module into another Python program and generate a student's result.

# student.py

# def total(marks):
#     return sum(marks)

# def percentage(marks):
#     return sum(marks)/len(marks)

# def grade(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 75:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "F"


# main.py

# import student

# marks = []

# for i in range(5):
#     mark = float(input("enter marks: "))
#     marks.append(mark)

# total = student.total(marks)
# percentage = student.percentage(marks)
# grade = student.grade(percentage)

# print("total =",total)
# print("percentage =",percentage)
# print("grade =",grade)


# 3. Create a module number_utils.py containing functions to check whether a number is prime, palindrome, Armstrong, or perfect. Import the required functions into a main program.

# number_utils.py

# def prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2,n):
#         if n%i == 0:
#             return False
    
#     return True


# def palindrome(n):
#     s = str(n)
#     return s == s[::-1]


# def armstrong(n):
#     s = str(n)
#     total = 0
    
#     for i in s:
#         total += int(i)**len(s)
    
#     return total == n


# def perfect(n):
#     total = 0
    
#     for i in range(1,n):
#         if n%i == 0:
#             total += i
    
#     return total == n


# main.py

# from number_utils import prime,palindrome,armstrong,perfect

# n = int(input("enter number: "))

# if prime(n):
#     print("prime number")
# else:
#     print("not prime number")

# if palindrome(n):
#     print("palindrome number")
# else:
#     print("not palindrome number")

# if armstrong(n):
#     print("armstrong number")
# else:
#     print("not armstrong number")

# if perfect(n):
#     print("perfect number")
# else:
#     print("not perfect number")


# 4. Create a module string_utils.py containing functions to count vowels, reverse a string, check palindrome, count words, and remove spaces.

# string_utils.py

# def count_vowels(s):
#     count = 0
    
#     for i in s:
#         if i.lower() in "aeiou":
#             count += 1
    
#     return count


# def reverse(s):
#     return s[::-1]


# def palindrome(s):
#     return s == s[::-1]


# def count_words(s):
#     return len(s.split())


# def remove_spaces(s):
#     return s.replace(" ","")


# main.py

# from string_utils import count_vowels,reverse,palindrome,count_words,remove_spaces

# s = input("enter string: ")

# print("vowels =",count_vowels(s))
# print("reverse =",reverse(s))
# print("palindrome =",palindrome(s))
# print("words =",count_words(s))
# print("without spaces =",remove_spaces(s))


# 5. Create a module containing functions to calculate gross salary, deductions, and net salary for an employee.

# salary.py

# def gross_salary(basic,allowance):
#     return basic + allowance

# def deductions(gross):
#     return gross*0.10

# def net_salary(gross,deduction):
#     return gross-deduction


# main.py

# import salary

# basic = float(input("enter basic salary: "))
# allowance = float(input("enter allowance: "))

# gross = salary.gross_salary(basic,allowance)
# deduction = salary.deductions(gross)
# net = salary.net_salary(gross,deduction)

# print("gross salary =",gross)
# print("deductions =",deduction)
# print("net salary =",net)


# 6. Create a module containing recursive functions for factorial, Fibonacci series, sum of digits, and binary conversion. Import and use these functions from another program.

# recursive.py

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
    
#     return n*factorial(n-1)


# def fibonacci(n):
#     if n <= 1:
#         return n
    
#     return fibonacci(n-1)+fibonacci(n-2)


# def sum_digits(n):
#     if n == 0:
#         return 0
    
#     return n%10 + sum_digits(n//10)


# def binary(n):
#     if n == 0:
#         return ""
    
#     return binary(n//2) + str(n%2)


# main.py

# from recursive import factorial,fibonacci,sum_digits,binary

# n = int(input("enter number: "))

# print("factorial =",factorial(n))
# print("fibonacci =",fibonacci(n))
# print("sum of digits =",sum_digits(n))
# print("binary =",binary(n))


# 7. Create a package named mathutils containing:
# basic.py – arithmetic operations
# number.py – prime, Armstrong, palindrome functions
# statistics.py – mean, maximum, minimum
# Create a main program that imports functions from each module.

# mathutils/basic.py

# def addition(a,b):
#     return a+b

# def subtraction(a,b):
#     return a-b

# def multiplication(a,b):
#     return a*b

# def division(a,b):
#     return a/b


# mathutils/number.py

# def prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2,n):
#         if n%i == 0:
#             return False
    
#     return True


# def armstrong(n):
#     s = str(n)
#     total = 0
    
#     for i in s:
#         total += int(i)**len(s)
    
#     return total == n


# def palindrome(n):
#     s = str(n)
#     return s == s[::-1]


# mathutils/statistics.py

# def mean(numbers):
#     return sum(numbers)/len(numbers)

# def maximum(numbers):
#     return max(numbers)

# def minimum(numbers):
#     return min(numbers)


# main.py

# from mathutils.basic import addition,subtraction,multiplication,division
# from mathutils.number import prime,armstrong,palindrome
# from mathutils.statistics import mean,maximum,minimum

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# print("addition =",addition(a,b))
# print("subtraction =",subtraction(a,b))
# print("multiplication =",multiplication(a,b))
# print("division =",division(a,b))

# n = int(input("enter number: "))

# print("prime =",prime(n))
# print("armstrong =",armstrong(n))
# print("palindrome =",palindrome(n))

# numbers = [10,20,30,40,50]

# print("mean =",mean(numbers))
# print("maximum =",maximum(numbers))
# print("minimum =",minimum(numbers))


# 8. Create a package student containing:
# marks.py – total and percentage
# grade.py – grade calculation
# attendance.py – attendance eligibility
# Write a main program that uses all three modules to generate a student report.

# student/marks.py

# def total(marks):
#     return sum(marks)

# def percentage(marks):
#     return sum(marks)/len(marks)


# student/grade.py

# def grade(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 75:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "F"


# student/attendance.py

# def eligibility(attended,total):
#     percentage = (attended/total)*100
    
#     if percentage >= 75:
#         return True
#     else:
#         return False


# main.py

# from student.marks import total,percentage
# from student.grade import grade
# from student.attendance import eligibility

# marks = []

# for i in range(5):
#     mark = float(input("enter marks: "))
#     marks.append(mark)

# attended = int(input("enter attended classes: "))
# total_classes = int(input("enter total classes: "))

# total_marks = total(marks)
# percent = percentage(marks)
# result = grade(percent)
# eligible = eligibility(attended,total_classes)

# print("total marks =",total_marks)
# print("percentage =",percent)
# print("grade =",result)

# if eligible:
#     print("attendance eligible")
# else:
#     print("attendance not eligible")


# 9. Develop a package banking containing:
# account.py – account creation and balance
# transaction.py – deposit and withdrawal
# loan.py – loan calculation
# Create a main program to use the package.

# banking/account.py

# def create_account(name,account_number,balance):
#     return {
#         "name":name,
#         "account_number":account_number,
#         "balance":balance
#     }

# def balance(account):
#     return account["balance"]


# banking/transaction.py

# def deposit(account,amount):
#     account["balance"] += amount
#     return account["balance"]

# def withdrawal(account,amount):
#     if amount <= account["balance"]:
#         account["balance"] -= amount
#     else:
#         print("insufficient balance")
    
#     return account["balance"]


# banking/loan.py

# def loan(principal,rate,time):
#     interest = principal*rate*time/100
#     return principal + interest


# main.py

# from banking.account import create_account,balance
# from banking.transaction import deposit,withdrawal
# from banking.loan import loan

# name = input("enter name: ")
# account_number = input("enter account number: ")
# amount = float(input("enter initial balance: "))

# account = create_account(name,account_number,amount)

# print("balance =",balance(account))

# deposit_amount = float(input("enter deposit amount: "))
# deposit(account,deposit_amount)

# print("balance =",balance(account))

# withdrawal_amount = float(input("enter withdrawal amount: "))
# withdrawal(account,withdrawal_amount)

# print("balance =",balance(account))

# principal = float(input("enter loan amount: "))
# rate = float(input("enter interest rate: "))
# time = float(input("enter time: "))

# print("loan amount =",loan(principal,rate,time))


# 10. Create a package texttools containing:
# cleaning.py – remove punctuation and extra spaces
# tokenization.py – tokenize text
# frequency.py – word-frequency analysis
# Create a main program to use the package.

# texttools/cleaning.py

# import string

# def remove_punctuation(s):
#     for i in string.punctuation:
#         s = s.replace(i,"")
    
#     return s

# def remove_extra_spaces(s):
#     return " ".join(s.split())


# texttools/tokenization.py

# def tokenize(s):
#     return s.split()


# texttools/frequency.py

# def frequency(s):
#     words = s.split()
#     result = {}
    
#     for i in words:
#         if i in result:
#             result[i] += 1
#         else:
#             result[i] = 1
    
#     return result


# main.py

# from texttools.cleaning import remove_punctuation,remove_extra_spaces
# from texttools.tokenization import tokenize
# from texttools.frequency import frequency

# s = input("enter text: ")

# s = remove_punctuation(s)
# s = remove_extra_spaces(s)

# print("clean text =",s)
# print("tokens =",tokenize(s))
# print("frequency =",frequency(s))


# 11. Create the following directory structure:
# college_project/
# main.py
# student/
# __init__.py
# details.py
# marks.py
# faculty/
# __init__.py
# details.py
# Write a program that imports functions from both packages and displays student and faculty information.

# student/details.py

# def student_details():
#     print("student name = Amit")
#     print("roll number = 101")
#     print("branch = CSE")


# student/marks.py

# def marks():
#     print("python = 85")
#     print("maths = 90")
#     print("os = 88")


# faculty/details.py

# def faculty_details():
#     print("faculty name = Rahul")
#     print("department = CSE")
#     print("experience = 5 years")


# main.py

# from student.details import student_details
# from student.marks import marks
# from faculty.details import faculty_details

# print("student details:")
# student_details()

# print("student marks:")
# marks()

# print("faculty details:")
# faculty_details()


# 12. Create a directory structure for a library application with separate packages for:
# Books
# Members
# Transactions
# Each package should contain suitable modules and a main program should combine all functionality.

# library/books/book.py

# def add_book(id,title):
#     print("book added")
#     print("book id =",id)
#     print("title =",title)


# library/members/member.py

# def add_member(id,name):
#     print("member added")
#     print("member id =",id)
#     print("name =",name)


# library/transactions/transaction.py

# def issue_book(book,member):
#     print("book issued")
#     print("book =",book)
#     print("member =",member)

# def return_book(book,member):
#     print("book returned")
#     print("book =",book)
#     print("member =",member)


# main.py

# from library.books.book import add_book
# from library.members.member import add_member
# from library.transactions.transaction import issue_book,return_book

# book_id = input("enter book id: ")
# title = input("enter book title: ")

# member_id = input("enter member id: ")
# name = input("enter member name: ")

# add_book(book_id,title)
# add_member(member_id,name)

# issue_book(title,name)
# return_book(title,name)


# 13. Create a directory named ecommerce containing packages for:
# Products
# Customers
# Orders
# Payments
# Each package should contain at least two modules.

# ecommerce/products/product.py

# def add_product(id,name,price):
#     print("product added")
#     print(id,name,price)


# ecommerce/products/category.py

# def category(name):
#     print("category =",name)


# ecommerce/customers/customer.py

# def add_customer(id,name):
#     print("customer added")
#     print(id,name)


# ecommerce/customers/address.py

# def address(city,state):
#     print("city =",city)
#     print("state =",state)


# ecommerce/orders/order.py

# def create_order(id,product):
#     print("order created")
#     print("order id =",id)
#     print("product =",product)


# ecommerce/orders/status.py

# def order_status(status):
#     print("order status =",status)


# ecommerce/payments/payment.py

# def payment(amount):
#     print("payment amount =",amount)


# ecommerce/payments/method.py

# def payment_method(method):
#     print("payment method =",method)


# main.py

# from ecommerce.products.product import add_product
# from ecommerce.products.category import category
# from ecommerce.customers.customer import add_customer
# from ecommerce.customers.address import address
# from ecommerce.orders.order import create_order
# from ecommerce.orders.status import order_status
# from ecommerce.payments.payment import payment
# from ecommerce.payments.method import payment_method

# product_id = input("enter product id: ")
# product_name = input("enter product name: ")
# price = float(input("enter price: "))

# add_product(product_id,product_name,price)

# product_category = input("enter category: ")
# category(product_category)

# customer_id = input("enter customer id: ")
# customer_name = input("enter customer name: ")

# add_customer(customer_id,customer_name)

# city = input("enter city: ")
# state = input("enter state: ")

# address(city,state)

# order_id = input("enter order id: ")

# create_order(order_id,product_name)

# order_status("confirmed")

# payment(price)

# payment_method("UPI")


# 14. Create a project directory containing packages for:
# Patient management
# Doctor management
# Billing
# Medical records
# Implement simple functions in each module and access them from main.py.

# medical_project/patient/patient.py

# def patient_details(name,age):
#     print("patient name =",name)
#     print("patient age =",age)


# medical_project/patient/registration.py

# def register_patient(id):
#     print("patient registered")
#     print("patient id =",id)


# medical_project/doctor/doctor.py

# def doctor_details(name,department):
#     print("doctor name =",name)
#     print("department =",department)


# medical_project/doctor/appointment.py

# def appointment(date):
#     print("appointment date =",date)


# medical_project/billing/bill.py

# def calculate_bill(amount):
#     print("total bill =",amount)


# medical_project/billing/payment.py

# def payment(amount):
#     print("payment received =",amount)


# medical_project/records/record.py

# def add_record(disease,medicine):
#     print("disease =",disease)
#     print("medicine =",medicine)


# medical_project/records/history.py

# def history():
#     print("medical history displayed")


# main.py

# from medical_project.patient.patient import patient_details
# from medical_project.patient.registration import register_patient
# from medical_project.doctor.doctor import doctor_details
# from medical_project.doctor.appointment import appointment
# from medical_project.billing.bill import calculate_bill
# from medical_project.billing.payment import payment
# from medical_project.records.record import add_record
# from medical_project.records.history import history

# patient_id = input("enter patient id: ")
# patient_name = input("enter patient name: ")
# age = int(input("enter patient age: "))

# register_patient(patient_id)
# patient_details(patient_name,age)

# doctor_name = input("enter doctor name: ")
# department = input("enter department: ")

# doctor_details(doctor_name,department)

# date = input("enter appointment date: ")

# appointment(date)

# disease = input("enter disease: ")
# medicine = input("enter medicine: ")

# add_record(disease,medicine)

# amount = float(input("enter bill amount: "))

# calculate_bill(amount)
# payment(amount)

# history()
