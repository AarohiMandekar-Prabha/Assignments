class Student:

    school_name = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        print("Student Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)
        print("School Name :", Student.school_name)
        print()

    @classmethod
    def change_school_name(cls, new_school):
        cls.school_name = new_school


student1 = Student("Soham", 19, "AIML")
student2 = Student("Rahul", 20, "Computer")

print("Before Changing School Name")
student1.display_student()
student2.display_student()

Student.change_school_name("XYZ College")

print("After Changing School Name")
student1.display_student()
student2.display_student()

class Employee:

    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

        Employee.employee_count += 1

    def display_employee(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Salary :", self.salary)
        print()

    @classmethod
    def show_total_employees(cls):
        print("Total Employees :", cls.employee_count)


employee1 = Employee(101, "Rahul", 35000)
employee2 = Employee(102, "Soham", 45000)
employee3 = Employee(103, "Amit", 50000)

employee1.display_employee()
employee2.display_employee()
employee3.display_employee()

Employee.show_total_employees()

class BankAccount:

    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance :", self.balance)

    @classmethod
    def change_bank_name(cls, new_bank):
        cls.bank_name = new_bank


account1 = BankAccount(101, "Soham", 10000)
account2 = BankAccount(102, "Rahul", 15000)

print("Bank Name :", BankAccount.bank_name)
print()

account1.deposit(2000)
account1.check_balance()

print()

account1.withdraw(3000)
account1.check_balance()

print()

BankAccount.change_bank_name("HDFC Bank")

print("New Bank Name :", BankAccount.bank_name)

class Mobile:

    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        print()

    def calculate_discount_price(self):
        discount = (self.price * Mobile.discount_percentage) / 100
        final_price = self.price - discount

        print("Discount Percentage :", Mobile.discount_percentage, "%")
        print("Discount Price :", final_price)
        print()

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount


mobile1 = Mobile("Apple", "iPhone 16", 80000)
mobile2 = Mobile("Samsung", "S25", 70000)
mobile3 = Mobile("OnePlus", "13", 60000)

print("Before Changing Discount")
mobile1.display_mobile()
mobile1.calculate_discount_price()

mobile2.display_mobile()
mobile2.calculate_discount_price()

mobile3.display_mobile()
mobile3.calculate_discount_price()

Mobile.change_discount(20)

print("After Changing Discount")

mobile1.calculate_discount_price()
mobile2.calculate_discount_price()
mobile3.calculate_discount_price()

class Library:

    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print("Book ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Library :", Library.library_name)
        print()

    @classmethod
    def change_library_name(cls, new_library):
        cls.library_name = new_library


book1 = Library(101, "Python Programming", "Guido")
book2 = Library(102, "Data Science", "James")
book3 = Library(103, "Machine Learning", "Andrew")

print("Before Changing Library Name")
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()

Library.change_library_name("Smart City Library")

print("After Changing Library Name")
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()