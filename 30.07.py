# n = int(input(" enter number:"))

# for i in range(n+1):
#     print(i)

# sum = 0
# for i in range(n+1):
#     sum = sum+i
# print(sum)

# l=[]
# b = []
# for i in range(1,n+1):
#     if i % 2 == 0:
#         l.append(i)
#     else:
#         b.append(i)
# print("EVEN - ",l)
# print("ODD - ",b)

# c=[]
# for i in range(n+1):
#    if i%2==0:
#        c.append(i**2)
# print(c) 

# l = 1
# for i in range(n):
#     print(l,end = " ")
#     l *=2

# for i in range (n):
#     print("A B C")

# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end = " ")
#     print()

# for i in range (n,0,-1):
#     for j in range(i):
#         print(chr(65+j),end = " ")
#     print()
        
        
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()

# i = 1    
# while i<=n:
#     print(i)
#     i+=1

# i = 1
# a=[]
# b=[]
# while i<=n:
#     if i%2==0:
#         a.append(i)
#         i+=1
#     else:
#         b.append(i)
#         i+=1
# print("even - ",a)
# print("odd - ",b)

# i = 1
# sum = 0
# while i<=n:
#     sum +=i
#     i+=1
# print(sum)

  
# while n>0:
#     print(n,end = " ")
#     n-=1

# even_sum = 0
# odd_sum =0
# i =1
# while i<=n:
#     if i%2 == 0:
#         even_sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print("even sum : ",even_sum)
# print("odd sum : ",odd_sum)

# temp = abs(n)
# sum = 0
# while temp>0:
#     digit = temp%10
#     sum +=digit
#     temp = temp//10
# print(sum)

# temp = n
# reverse = 0
# while temp>0:
#     digit = temp%10
#     reverse = (reverse*10)+digit
#     temp = temp//10
# if n == reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")


# if n == 0:
#     print("zero")
# else:
#     print("non zero")


# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# if a > b:
#     print(a,"is largest")
# else:
#     print(b,"is largest")


# if n > 0:
#     print("positive")
# elif n < 0:
#     print("negative")
# else:
#     print("zero")


# ch = input("enter character: ")
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
#     print("vowel")
# else:
#     print("consonant")


# p = int(input("enter percentage: "))
# if p >= 90:
#     print("Excellent performance")
# elif p>=80:
#     print("Very good performance")
# elif p>=70:
#     print("Good performance")
# elif p>=60:
#     print("Average performance")
# else:
#     print("Poor performance")


# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
# if a > b and a > c:
#     print(a,"is largest")
# elif b > a and b > c:
#     print(b,"is largest")
# else:
#     print(c,"is largest")

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
# if a < b and a < c:
#     print(a,"is smallest")
# elif b < a and b < c:
#     print(b,"is smallest")
# else:
#     print(c,"is smallest")


# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")


# year = int(input("enter year: "))
# if year % 400 == 0:
#     print("leap year")
# elif year % 100 == 0:
#     print("not a leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("not a leap year")


# married = input("are you married yes/no: ")
# gender = input("enter gender male/female: ")
# age = int(input("enter age: "))
# if married == "yes":
#     print("insured")
# elif gender == "male" and age > 30:
#     print("insured")
# elif gender == "female" and age > 25:
#     print("insured")
# else:
#     print("not insured")