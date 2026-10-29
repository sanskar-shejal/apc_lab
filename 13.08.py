#Student Grade Management System
names = []
grades = []

def add_student():
    name = input("enter student name: ")
    grade = float(input("enter grade: "))
    names.append(name)
    grades.append(grade)
    print("student added")

def update_grade():
    name = input("enter student name: ")
    if name in names:
        index = names.index(name)
        grade = float(input("enter new grade: "))
        grades[index] = grade
        print("grade updated")
    else:
        print("student not found")

def remove_student():
    name = input("enter student name: ")
    if name in names:
        index = names.index(name)
        names.pop(index)
        grades.pop(index)
        print("student removed")
    else:
        print("student not found")

def average_grade():
    if len(grades) > 0:
        total = 0
        for i in grades:
            total += i
        print("average grade =",total/len(grades))
    else:
        print("no grades available")

def extreme_grades():
    if len(grades) > 0:
        highest = grades[0]
        lowest = grades[0]
        for i in grades:
            if i > highest:
                highest = i
            if i < lowest:
                lowest = i
        print("highest grade =",highest)
        print("lowest grade =",lowest)
    else:
        print("no grades available")

add_student()
add_student()
update_grade()
remove_student()
average_grade()
extreme_grades()


#Point Management System
def distance(p1,p2):
    x = p2[0]-p1[0]
    y = p2[1]-p1[1]
    return (x*x+y*y)**0.5

def farthest_point(points):
    farthest = points[0]
    distance1 = (points[0][0]**2+points[0][1]**2)**0.5
    for i in points:
        distance2 = (i[0]**2+i[1]**2)**0.5
        if distance2 > distance1:
            distance1 = distance2
            farthest = i
    return farthest

points = []
n = int(input("enter number of points: "))

for i in range(n):
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    points.append((x,y))

p1 = points[0]
p2 = points[1]

print("distance =",distance(p1,p2))
print("farthest point =",farthest_point(points))


#Web Server Configuration
server_ip = (192,168,1,1)
allowed_ips = ["192.168.1.2","192.168.1.3"]

def update_allowed():
    ip = input("enter ip to add: ")
    allowed_ips.append(ip)

def display_config():
    print("server ip =",server_ip)
    print("allowed ips =",allowed_ips)

update_allowed()
display_config()


#Project Employee Analysis
project1 = {"Amit","Rahul","Chetan","Rohit"}
project2 = {"Chetan","Rohit","Sneha","Priya"}

print("employees in both projects =",project1.intersection(project2))
print("employees only in project 1 =",project1.difference(project2))
print("employees only in project 2 =",project2.difference(project1))
print("total unique employees =",project1.union(project2))


#Text Analysis Tool
s = input("enter paragraph: ")
words = s.split()

print("total words =",len(words))

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

for i in frequency:
    print(i,"=",frequency[i])

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 3 most frequent words:")
for i in range(min(3,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])

vowel = 0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowel +=1

print("vowels =",vowel)


#Vocabulary Analysis
book1 = input("enter first book text: ")
book2 = input("enter second book text: ")

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

print("unique words in first book =",words1)
print("unique words in second book =",words2)
print("common words =",words1.intersection(words2))
print("words unique to first book =",words1.difference(words2))
print("words unique to second book =",words2.difference(words1))
print("total unique words =",len(words1.union(words2)))


#Inventory System
inventory = {}

def add_product():
    name = input("enter product name: ")
    quantity = int(input("enter quantity: "))
    inventory[name] = quantity
    print("product added")

def update_product():
    name = input("enter product name: ")
    if name in inventory:
        quantity = int(input("enter new quantity: "))
        inventory[name] = quantity
        print("quantity updated")
    else:
        print("product not found")

def remove_product():
    name = input("enter product name: ")
    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("product removed")
        else:
            print("quantity is not zero")
    else:
        print("product not found")

def highest_stock():
    if len(inventory) > 0:
        product = ""
        highest = 0
        for i in inventory:
            if inventory[i] > highest:
                highest = inventory[i]
                product = i
        print("highest stock product =",product)
        print("quantity =",highest)

add_product()
add_product()
update_product()
highest_stock()
remove_product()
print("total unique products =",len(inventory))


#Anagram Check
a = input("enter first string: ")
b = input("enter second string: ")

x = ""
y = ""

for i in a:
    if i.isalnum():
        x += i.lower()

for i in b:
    if i.isalnum():
        y += i.lower()

if sorted(x) == sorted(y):
    print("anagram")
else:
    print("not anagram")


#Attendance System
attendance = {
    "Monday":{"Amit","Rahul","Chetan"},
    "Tuesday":{"Amit","Chetan","Rohit"},
    "Wednesday":{"Amit","Chetan"},
    "Thursday":{"Amit","Rahul","Chetan"},
    "Friday":{"Amit","Chetan","Sneha"}
}

all_students = set()

for i in attendance:
    all_students = all_students.union(attendance[i])

all_attended = set(all_students)

for i in attendance:
    all_attended = all_attended.intersection(attendance[i])

print("students who attended all classes =",all_attended)

only_one = set()

for i in all_students:
    count = 0
    for j in attendance:
        if i in attendance[j]:
            count +=1
    if count == 1:
        only_one.add(i)

print("students who attended only one class =",only_one)
print("total unique students =",len(all_students))


#Character Frequency
s = input("enter string: ")
choice = input("ignore case? yes/no: ")

frequency = {}

for i in s:
    if choice == "yes":
        ch = i.lower()
    else:
        ch = i

    if ch in frequency:
        frequency[ch] +=1
    else:
        frequency[ch] =1

sorted_frequency = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

for i in sorted_frequency:
    print(i[0],"=",i[1])


#Email Validator using Regular Expression
import re

email = input("enter email: ")

pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+\.[a-zA-Z]{2,6}$"

if re.match(pattern,email):
    print("valid email")
else:
    print("invalid email")


#Phone Number Extraction
import re

s = input("enter text: ")

pattern = r"(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{10})"

numbers = re.findall(pattern,s)

print("phone numbers =",numbers)


#URL Extraction
import re

s = input("enter html content: ")

pattern = r"(https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

urls = re.findall(pattern,s)

print("urls =",urls)


#Password Strength Checker using Regular Expression
import re

password = input("enter password: ")

if len(password) >= 8 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[0-9]",password) and re.search(r"[!@#$%^&*()_-]",password):
    print("strong password")
else:
    print("weak password")


#Date Extraction
import re

s = input("enter text: ")

pattern1 = r"\b\d{2}/\d{2}/\d{4}\b"
pattern2 = r"\b\d{2}-\d{2}-\d{4}\b"
pattern3 = r"\b\d{4}\.\d{2}\.\d{2}\b"
pattern4 = r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b"

dates = re.findall(pattern1,s)
dates += re.findall(pattern2,s)
dates += re.findall(pattern3,s)
dates += re.findall(pattern4,s)

print("dates =",dates)


#HTML Tag Remover
import re

s = input("enter html content: ")

ans = re.sub(r"<[^>]*>","",s)

print(ans)


#Hashtag Extraction
import re

s = input("enter social media post: ")

hashtags = re.findall(r"#[a-zA-Z0-9_]+",s)

print("hashtags =",hashtags)


#File Extension Counter
import re

files = input("enter filenames separated by space: ").split()

extensions = {}

for i in files:
    match = re.search(r"\.([a-zA-Z0-9]+)$",i)
    if match:
        extension = "." + match.group(1)
        if extension in extensions:
            extensions[extension] +=1
        else:
            extensions[extension] =1

print(extensions)


#IP Address Validator
import re

ip = input("enter ip address: ")

ipv4 = r"^(\d{1,3}\.){3}\d{1,3}$"
ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

if re.match(ipv4,ip):
    parts = ip.split(".")
    valid = True
    for i in parts:
        if int(i) > 255:
            valid = False
    if valid:
        print("valid ip")
    else:
        print("invalid ip")
elif re.match(ipv6,ip):
    print("valid ip")
else:
    print("invalid ip")


#Word Count from File
import string

filename = input("enter file name: ")

file = open(filename,"r")
s = file.read()
file.close()

s = s.lower()

for i in string.punctuation:
    s = s.replace(i," ")

words = s.split()

print("total words =",len(words))

frequency = {}

for i in words:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 10 words:")

for i in range(min(10,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])


#Text Search and Highlight
s = input("enter text: ")
query = input("enter search query: ")

lower_s = s.lower()
lower_query = query.lower()

count = 0
position = 0

while True:
    position = lower_s.find(lower_query,position)

    if position == -1:
        break

    count +=1
    position += len(lower_query)

print("occurrences =",count)

ans = ""
i = 0

while i < len(s):
    if lower_s[i:i+len(query)] == lower_query:
        ans += "**" + s[i:i+len(query)] + "**"
        i += len(query)
    else:
        ans += s[i]
        i +=1

print(ans)


#Stopword Removal
s = input("enter paragraph: ")

stopwords = ["is","am","are","the","a","an","and","or","of","to","in","on","for","with"]

words = s.split()
ans = ""

for i in words:
    if i.lower() not in stopwords:
        ans += i + " "

print(ans)


#Find and Replace in Text File
filename = input("enter file name: ")
old = input("enter word to replace: ")
new = input("enter new word: ")
choice = input("case insensitive? yes/no: ")

file = open(filename,"r")
s = file.read()
file.close()

if choice == "yes":
    import re
    s = re.sub(re.escape(old),new,s,flags=re.IGNORECASE)
else:
    s = s.replace(old,new)

newfile = input("enter new file name: ")

file = open(newfile,"w")
file.write(s)
file.close()

print("file saved")


#Sentence Segmentation
import re

s = input("enter text: ")

abbreviations = ["Dr.","Mr.","Mrs.","Ms.","Prof."]

for i in abbreviations:
    s = s.replace(i,i.replace(".","<DOT>"))

sentences = re.split(r"[.!?]+",s)

for i in sentences:
    i = i.replace("<DOT>",".")

    if i.strip() != "":
        print(i.strip())


#Text Summarizer
s = input("enter text: ")

sentences = s.split(".")

words = s.lower().split()

frequency = {}

for i in words:
    if i in ["the","is","a","an","and","of","to","in","for","on"]:
        continue

    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

scores = []

for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        if word in frequency:
            score += frequency[word]
    scores.append((score,sentence.strip()))

scores = sorted(scores,reverse=True)

print("summary:")

for i in range(min(3,len(scores))):
    if scores[i][1] != "":
        print(scores[i][1])


#NLP Text Normalization
import re

s = input("enter text: ")

contractions = {
    "don't":"do not",
    "can't":"cannot",
    "won't":"will not",
    "isn't":"is not",
    "aren't":"are not",
    "wasn't":"was not",
    "weren't":"were not",
    "I'm":"I am",
    "I've":"I have",
    "I'll":"I will"
}

for i in contractions:
    s = s.replace(i,contractions[i])

s = s.lower()
s = re.sub(r"[^a-zA-Z\s]","",s)
s = re.sub(r"\d+","",s)

print(s)


#Palindrome Finder
import string

s = input("enter word or phrase: ")

ans = ""

for i in s:
    if i.isalnum():
        ans += i.lower()

reverse = ""

for i in ans:
    reverse = i + reverse

if ans == reverse:
    print("True")
else:
    print("False")


#Keyword Extraction
s = input("enter text: ")

stopwords = ["the","is","a","an","and","or","of","to","in","for","on","with","this","that"]

words = s.lower().split()

frequency = {}

for i in words:
    i = i.strip(".,!?;:")
    if i not in stopwords and i != "":
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] =1

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 5 keywords:")

for i in range(min(5,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])


#Simple Spell Checker
text = input("enter text: ")

dictionary = {
    "this","is","a","simple","text","hello","world","python",
    "program","student","computer","science","book","school",
    "college","good","bad","example","programming","language"
}

words = text.lower().split()
misspelled = []

for i in words:
    i = i.strip(".,!?;:")

    if i not in dictionary and i not in misspelled:
        misspelled.append(i)

print("misspelled words =",misspelled)


#Book Class
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "available"

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            print("book borrowed")
        else:
            print("book is already borrowed")

    def return_book(self):
        self.status = "available"
        print("book returned")

    def show_details(self):
        print("title =",self.title)
        print("author =",self.author)
        print("year =",self.year)
        print("status =",self.status)

book = Book("Python Programming","John",2025)

book.show_details()
book.borrow()
book.show_details()
book.return_book()
book.show_details()


#Bank Account
class BankAccount:
    counter = 1000

    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount.counter
        BankAccount.counter +=1

    def deposit(self,amount):
        self.balance += amount
        print("amount deposited =",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("amount withdrawn =",amount)
        else:
            print("insufficient balance")

    def display_balance(self):
        print("account holder =",self.account_holder)
        print("account number =",self.account_number)
        print("balance =",self.balance)

    def transfer(self,amount,other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("transfer successful")
        else:
            print("insufficient balance")

account1 = BankAccount("Chetan")
account2 = BankAccount("Rahul")

account1.deposit(10000)
account1.withdraw(2000)
account1.transfer(3000,account2)

account1.display_balance()
account2.display_balance()


#Person and Employee
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("name =",self.name)
        print("age =",self.age)

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("employee id =",self.employee_id)
        print("salary =",self.salary)

employee = Employee("Chetan",20,"EMP101",50000)

employee.display_employee_info()


#Multilevel Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print("name =",self.name)
        print("age =",self.age)

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        self.display_person_info()
        print("employee id =",self.employee_id)
        print("salary =",self.salary)

class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department,team_size):
        super().__init__(name,age,employee_id,salary)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self):
        self.display_employee_info()
        print("department =",self.department)
        print("team size =",self.team_size)

manager = Manager("Chetan",20,"M101",80000,"IT",10)

manager.display_manager_info()


#Calculator
class Calculator:
    def add(self,a,b,c=0,d=0):
        return a+b+c+d

calculator = Calculator()

print("addition of two numbers =",calculator.add(10,20))
print("addition of three numbers =",calculator.add(10,20,30))
print("addition of four numbers =",calculator.add(10,20,30,40))