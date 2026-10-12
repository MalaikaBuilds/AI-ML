#library management system
"""
Features:                       core module: 
add                       member management             
issue                      circulation module
return                     book management.........
View                       fine managment..........
Exit   
"""
print("Welcome to my library")

library = []
fines = {}          # empty dictionary

n = int(input("How many books do you want to add? "))

for i in range(n):
    book = input(f"Enter book {i+1}: ")
    library.append(book)

print("\nBooks in library:")
for book in library:
    print(book)

def add_book():
    book = input("Enter a book name to be added: ")
    library.append(book)
    print(f"'{book}' has been added")

def issue_book():
    book = input("Enter book name to be issued: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' has been issued")
    else:
        print("Book not found")
def return_book():
    book = input("Enter book name to be returned: ")
    library.append(book)
    print(f"'{book}' has been returned")
    late = input("Was the book returned late? (yes/no): ")
    if late.lower() == "yes":
        days = int(input("Enter number of late days: "))
        fine = days * 10   
        fines[book] = fine
        print(f"Fine of Rs.{fine} added for '{book}'")
def view_book():
    if not library:
        print("No books are present in the library")
    else:
        print("List of books:")
        idx = 1
        for book in library:
            print(f"{idx}. {book}")
            idx += 1
def view_fines():
    if not fines:
        print("No fines pending")
    else:
        print("Pending Fines:")
        for book, fine in fines.items():
            print(f"{book} : Rs.{fine}")
def pay_fine():
    book = input("Enter book name to pay fine for: ")
    if book in fines:
        print(f"Fine Amount: Rs.{fines[book]}")
        del fines[book]
        print("Fine paid successfully")
    else:
        print("No fine found for this book")

while True:
    print("------ Library Management System ------")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. View Fines")
    print("6. Pay Fine")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        view_book()
    elif choice == 5:
        view_fines()
    elif choice == 6:
        pay_fine()
    elif choice == 7:
        print("Thank you, you are now exiting library system")
        break
    else:
        print("Invalid choice. Try again.")