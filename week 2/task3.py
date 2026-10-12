#function
#Function to Count Words in a Sentence
def count_words(sentence):        #split break a sentence into list of words
    words = sentence.split()
    return len(words)
print(count_words("My Name is Malaika Shakil"))
print(count_words("Hello Malaika"))

#Write a function `calculate_discount(price, percent)` that returns the final price after applying a discount.  
def calculate_discount(price, percent):
    discount = (price * percent) / 100
    final_price = price - discount
    return final_price
print(calculate_discount(1000, 10))
print(calculate_discount(500, 20))

#Function Scope
#Create a global variable `count = 100` and print it both inside and outside a function  
count = 100   # Global variable
def show_count():
    print("Inside function:", count)
show_count()
print("Outside function:", count)

#10. Write a program with: 
"""
One global variable 
One local variable 
One nested function 
"""
count = 100   # Global variable
def my_func():
    age = 20   # Local variable
    def inner_function():
        print("Inside inner function:")
        print("Global variable count =", count)
        print("Local variable age =", age)
    inner_function()
    print("Inside outer function:")
    print("Local variable age =", age)
my_func()
print("Outside function:")
print("Global variable count =", count)

#lambda function
#Find the Larger Number
max = lambda a, b: a if a > b else b
print(max(15, 10))

#Write a lambda function that checks whether a number is positive or negative.  
check_num = lambda n: "Positive" if n > 0 else "Negative"
print(check_num(10))
print(check_num(-5))

#Map & Filters
#Sort Names by Length
names = ["Ali", "Ahmed", "Sara", "Zainab"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
#Keep Names Longer Than 4 Characters
names = ["Ali", "Ahmed", "Sara", "Zainab"]
result = list(filter(lambda name: len(name) > 4, names))
print(result)

#inner/nested function
#Find Square and Cube
def calculate(n):
    def square():
        return n * n
    def cube():
        return n * n * n
    print("Square =", square())
    print("Cube =", cube())
calculate(3)
#Nested Function Accessing Outer Variable
def outer():
    x = 10
    def inner():
        print("Value of x =", x)
    inner()
outer()