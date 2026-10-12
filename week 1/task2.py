#Ternary expression
#Assign:
"""
- "Fri" if num is 5
- "Sat" if num is 6
- "Sun" if num is 7
- otherwise assign "weekday":
"""
num=int(input("enter your num"))
x="Fri" if num==5 else "Sat" if num ==6 else "Sun" if num==7 else "weekday"
print(x)

#Check if a number is even or odd
num=int(input("enter your num"))
x="even"if num %2 ==0 else "odd"
print(x)

#Check if a year is a leap year
year=int(input("enter ur year"))
x="leap year" if year%4==0 else "not a leap year"
print(x)

#Check if a person can vote
age=int(input("enter your age"))
x="can vote" if age>=18 else "not eligible for vote"
print(x)

#Find the largest of three numbers
a = 10
b = 25
c = 18
x="largest" if a>b and b>c else (b if a<c else c)
print(x)

#Break,pass,cotinue
#Print characters except vowels
word = "PYTHONPROGRAM"
for i in word:
    if i in "AEIOU":
        continue
    print(i)
    
#Stop a password loop
password = "malaika"
while True:
    user_input=input("Enter password")
    if user_input == password:
        print("accepted")
        break
    print("denied")

#for loop & enumerate    
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
for index, color in enumerate(colors):
    if index % 2 == 0:
        print(color)
        
#Number each word in a sentence
words = ["Python", "Java", "C++", "JavaScript"]
for num, word in enumerate(words, start=1):
    print(f"{num}. {word}")

#While loop
#Sum of first 10 natural numbers
num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print("Sum =", total)

#Multiplication table of a number
num = 12
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

#nested loop
#Print a square pattern
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
#Multiplication Table (1 to 5)
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
#Number Pattern
for i in range(1, 6):            #i outer loop
    for j in range(1, i + 1):    #j inner loop
        print(j, end=" ")
    print()
#multiplication table of 12
for i in range (3,4):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
        print()
        