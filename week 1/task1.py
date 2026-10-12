#list
#Reverse the elements of a list.
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

#Add "Cherry" to the list ,remove "orange",first and last element of a list.

fruits = ["Apple", "Banana", "Orange", "Mango"]
fruits.append("Cherry")
fruits.remove("Orange")
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Updated List:", fruits)

#Tuple
#Count how many times 2 appears in a tuple.
NUM = (1, 2, 3, 2, 4, 2)
print(NUM.count(2))

#Find the index of 30.
numbers = (10, 20, 30, 40, 50)
print(numbers.index(30))

#Sets
#Find common elements in two sets.
A = {1, 2, 3}
B = {3, 4, 5}
print(A.intersection(B))

#Remove duplicates from the list [1, 2, 2, 3, 4, 4, 5].
list = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(list)
print(unique_values)

#Dictionaries
#Change the student's age to 21,and add grade

student = {
    "name": "Ali",
    "age": 20
}
student["age"] = 21
print(student)
student["grade"] = "A"
print(student)

#if/else/elif
#1:
#Number Divisibility Check
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3 only")
elif num % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")

#2:
# Login Verification
username = input("Username: ")
password = input("Password: ")

if username == "Malaika" and password == "1234":
    print("Login Successful")
else:
    print("Access Denied")

#3:
#ATM Withdrawal Check
balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
    
#4
#Electricity Bill Calculator
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 8
else:
    bill = units * 10
print("Bill =", bill)

#5
#BMI Calculator
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")