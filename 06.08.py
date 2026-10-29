#String Length
s = input("enter string: ")
count = 0
for i in s:
    count += 1
print("length =",count)

#Character Count
s = input("enter string: ")
vowel = 0
consonant = 0
digit = 0
space = 0
special = 0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowel +=1
    elif (i>="a" and i<="z") or (i>="A" and i<="Z"):
        consonant +=1
    elif i>="0" and i<="9":
        digit +=1
    elif i==" ":
        space +=1
    else:
        special +=1
print("vowels =",vowel)
print("consonants =",consonant)
print("digits =",digit)
print("spaces =",space)
print("special characters =",special)

#Reverse a String
s = input("enter string: ")
reverse = ""
for i in s:
    reverse = i + reverse
print(reverse)

#palindrome check
s = input("enter string: ")
reverse = ""
for i in s:
    reverse = i + reverse
if s == reverse:
    print("palindrome")
else:
    print("not palindrome")
    
#Uppercase and Lowercase Count
s = input("enter string: ")
upper = 0
lower = 0
for i in s:
    if i>="A" and i<="Z":
        upper +=1
    elif i>="a" and i<="z":
        lower +=1
print("uppercase =",upper)
print("lowercase =",lower)

#Replace Characters
s = input("enter string: ")

old = input("enter character to replace: ")
new = input("enter new character: ")
ans = ""
for i in s:
    if i == old:
        ans += new
    else:
        ans += i
print(ans)

#Remove Spaces
s = input("enter string: ")
ans = ""
for i in s:
    if i != " ":
        ans += i
print(ans)

#Frequency of a Character
s = input("enter string: ")
ch = input("enter character: ")
count = 0
for i in s:
    if i == ch:
        count +=1
print(ch,"appears",count,"times")

#First and Last Character
s = input("enter string: ")
print("first character =",s[0])
print("last character =",s[-1])

#ASCII Values
s = input("enter string: ")
for i in s:
    print(i,"=",ord(i))
    
#Word Count
s = input("enter sentence: ")
count = 0
word = False
for i in s:
    if i != " " and word == False:
        count +=1
        word = True
    elif i == " ":
        word = False
print("total words =",count)

#Longest Word
s = input("enter sentence: ")
word = ""
longest = ""
for i in s:
    if i != " ":
        word += i
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
if len(word) > len(longest):
    longest = word
print("longest word =",longest)

#Shortest Word
s = input("enter sentence: ")
word = ""
shortest = ""
first = True
for i in s:
    if i != " ":
        word += i
    else:
        if first == True:
            shortest = word
            first = False
        elif len(word) < len(shortest):
            shortest = word
        word = ""
if first == True:
    shortest = word
elif len(word) < len(shortest):
    shortest = word
print("shortest word =",shortest)

#Title Case
s = input("enter sentence: ")
ans = ""
new = True
for i in s:
    if new == True and i>="a" and i<="z":
        ans += chr(ord(i)-32)
        new = False
    else:
        ans += i
        if i == " ":
            new = True
        else:
            new = False
print(ans)

#Duplicate Characters
s = input("enter string: ")
printed = ""
for i in s:
    count = 0
    for j in s:
        if i == j:
            count +=1
    if count > 1 and i not in printed:
        print(i)
        printed += i

#Character Frequency
s = input("enter string: ")
printed = ""
for i in s:
    if i not in printed:
        count = 0
        for j in s:
            if i == j:
                count +=1
        print(i,"=",count)
        printed += i

#Anagram Check
a = input("enter first string: ")
b = input("enter second string: ")
x = sorted(a)
y = sorted(b)
if x == y:
    print("anagram")
else:
    print("not anagram")

#Remove Duplicate Characters
s = input("enter string: ")
ans = ""
for i in s:
    if i not in ans:
        ans += i
print(ans)

#Substring Search
s = input("enter main string: ")
sub = input("enter substring: ")
if sub in s:
    print("substring found")
else:
    print("substring not found")
    
#Count Occurrences of a Word
s = input("enter sentence: ")
w = input("enter word: ")
word = ""
count = 0
for i in s+" ":
    if i != " ":
        word += i
    else:
        if word == w:
            count +=1
        word = ""
print(w,"appears",count,"times")

#Password Validator
password = input("enter password: ")
upper = 0
lower = 0
digit = 0
special = 0
count = 0
for i in password:
    count +=1
    if i>="A" and i<="Z":
        upper +=1
    elif i>="a" and i<="z":
        lower +=1
    elif i>="0" and i<="9":
        digit +=1
    else:
        special +=1
if count>=8 and upper>=1 and lower>=1 and digit>=1 and special>=1:
    print("valid password")
else:
    print("invalid password")

#Run-Length Encoding
s = input("enter string: ")
ans = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count +=1
    else:
        ans += s[i] + str(count)
        count = 1
ans += s[len(s)-1] + str(count)
print(ans)

#String Compression
s = input("enter string: ")
ans = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count +=1
    else:
        ans += s[i] + str(count)
        count = 1
ans += s[len(s)-1] + str(count)
if len(ans) < len(s):
    print(ans)
else:
    print(s)

#Most Frequent Character
s = input("enter string: ")
max = 0
ch = ""
for i in s:
    count = 0
    for j in s:
        if i == j:
            count +=1
    if count > max:
        max = count
        ch = i
print("most frequent character =",ch)

#Second Most Frequent Character
s = input("enter string: ")
max = 0
second = 0
firstch = ""
secondch = ""
printed = ""
for i in s:
    if i not in printed:
        count = 0
        for j in s:
            if i == j:
                count +=1
        if count > max:
            second = max
            secondch = firstch
            max = count
            firstch = i
        elif count > second and count < max:
            second = count
            secondch = i
        printed += i
print("second most frequent character =",secondch)

#Caesar Cipher
s = input("enter message: ")
key = int(input("enter key: "))
encrypt = ""
for i in s:
    if i>="a" and i<="z":
        encrypt += chr((ord(i)-97+key)%26+97)
    elif i>="A" and i<="Z":
        encrypt += chr((ord(i)-65+key)%26+65)
    else:
        encrypt += i
print("encrypted =",encrypt)
decrypt = ""
for i in encrypt:
    if i>="a" and i<="z":
        decrypt += chr((ord(i)-97-key)%26+97)
    elif i>="A" and i<="Z":
        decrypt += chr((ord(i)-65-key)%26+65)
    else:
        decrypt += i
print("decrypted =",decrypt)

#Email Validator
email = input("enter email: ")
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")

#Word Frequency Dictionary
s = input("enter paragraph: ")
words = s.split()
frequency = {}
for i in words:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1
for i in frequency:
    print(i,"=",frequency[i])

#Sentence Reversal
s = input("enter sentence: ")
words = s.split()
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
#String Rotation
a = input("enter first string: ")
b = input("enter second string: ")
if len(a) == len(b) and b in (a+a):
    print("yes")
else:
    print("no")