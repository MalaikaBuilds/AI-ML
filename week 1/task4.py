#Access Specifiers (Public, Protected, Private)
#in python, Access Specifiers (Access Modifiers) are used to control how attributes and methods of a class can be accessed.
#Public
#Accessible from anywhere.
#No underscore is used.
class Student:
    def __init__(self):
        self.name = "Ali"   # Public variable

s = Student()
print(s.name)
#Protected Access Specifier
#Indicated by a single underscore _.
#should be accessed only within the class and its subclasses (by convention).
class Student:
    def __init__(self):
        self._age = 20         # Protected variable

class Child(Student):
    def show(self):
        print(self._age)
c = Child()
c.show()
#private
#Indicated by double underscores __.
#Cannot be accessed directly outside the class
class Student:
    def __init__(self):
        self.__marks = 90   # Private variable

    def show_marks(self):
        print(self.__marks)

s = Student()
s.show_marks()
#Public	name	Anywhere
#Protected	_name	Class & Subclass (convention)
#Private	__name	Only inside the class

#name mangling
#Name mangling does not make a variable truly private; it simply renames it internally to reduce accidental access.
#To indicate that a variable is intended for internal use only.

#Nested class
#A Nested Class (Inner Class) is a class defined inside another class.
#It is used when one class logically belongs to another class.
class Student:
    class Laptop:
        def __init__(self):
            self.brand = "Dell"

        def show(self):
            print("Brand:", self.brand)
s = Student()
lap = Student.Laptop()
lap.show()

#aggregation
#Aggregation is a "Has-A" relationship in oop where one class contains an object of another class, but both objects can exist independently of each other.
class Department:
    def __init__(self, name):
        self.name = name
class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department   # Aggregation
dept = Department("Computer Science")     # Create Department object independently
teacher = Teacher("Ali", dept)          # Pass Department object to Teacher
print(teacher.name)
print(teacher.department.name)
#Association
#association means two classes are related to each other, but they can exist independently.
class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(self.name, "is teaching")
class Student:
    def __init__(self, name):
        self.name = name
    def learn(self):
        print(self.name, "is learning")
t1 = Teacher("Ali")
s1 = Student("Ahmed")
t1.teach()
s1.learn()
#Composition is a strong "Has-A" relationship where one object owns another object.
class Room:
    def __init__(self):
        print("Room Created")
class House:
    def __init__(self):
        self.room = Room()
    def show(self):
        print("House contains a room")
h1 = House()
h1.show()
