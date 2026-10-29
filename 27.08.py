#Email Validator using Regular Expression
# import re

# email = input("Enter email: ")

# pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*\.[a-zA-Z]{2,6}$"

# if re.match(pattern, email):
#     print("valid email")
# else:
#     print("invalid email")
    
# #Password Strength Checker using Regular Expression
# import re

# password = input("enter password: ")

# if len(password) >= 8 and re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[0-9]",password) and re.search(r"[!@#$%^&*()_-]",password):
#     print("strong password")
# else:
#     print("weak password")
    
    
# Hashtag Extraction
# import re

# s = input("enter social media post: ")

# hashtags = re.findall(r"#[a-zA-Z0-9_]+",s)

# print("hashtags =",hashtags)

#IP Address Validator
# import re

# ip = input("enter ip address: ")

# ipv4 = r"^(\d{1,3}\.){3}\d{1,3}$"
# ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

# if re.match(ipv4,ip):
#     parts = ip.split(".")
#     valid = True
#     for i in parts:
#         if int(i) > 255:
#             valid = False
#     if valid:
#         print("valid ip")
#     else:
#         print("invalid ip")
# elif re.match(ipv6,ip):
#     print("valid ip")
# else:
#     print("invalid ip")

#Word Count from File
# import string

# filename = input("enter file name: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# s = s.lower()

# for i in string.punctuation:
#     s = s.replace(i," ")

# words = s.split()

# print("total words =",len(words))

# frequency = {}

# for i in words:
#     if i in frequency:
#         frequency[i] +=1
#     else:
#         frequency[i] =1

# sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

# print("top 10 words:")

# for i in range(min(10,len(sorted_words))):
#     print(sorted_words[i][0],"=",sorted_words[i][1])

# #Find and Replace in Text File
# filename = input("enter file name: ")
# old = input("enter word to replace: ")
# new = input("enter new word: ")
# choice = input("case insensitive? yes/no: ")

# file = open(filename,"r")
# s = file.read()
# file.close()

# if choice == "yes":
#     import re
#     s = re.sub(re.escape(old),new,s,flags=re.IGNORECASE)
# else:
#     s = s.replace(old,new)

# newfile = input("Enter new File name: ")
# file = open(newfile,"w")
# file.write(s)
# file.close()
# print("file saved")
