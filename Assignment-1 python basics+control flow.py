print("Name: Aarohi Mandekar")
print("College: ABC College")
print("Favorite Programming Language: Python")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + ",", "you are", age, "years old.")


student_name = "Aarohi"
roll_number = 101
percentage = 87.5
passed = True

print("Student Details")
print("----------------")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Percentage   :", percentage, "%")
print("Passed       :", passed)


name1 = "Aarohi"
student_name = "Rahul"
class_name = "AIML-C"
total_marks = 450
user_name = "aarohi123"

print("name1 =", name1)
print("student_name =", student_name)
print("class_name =", class_name)
print("total_marks =", total_marks)
print("user_name =", user_name)


num = 25              
price = 99.99         
name = "Aarohi"       
passed = True         

print("num =", num, "Type:", type(num))
print("price =", price, "Type:", type(price))
print("name =", name, "Type:", type(name))
print("passed =", passed, "Type:", type(passed))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum =",total)


decimal_num = float(input("Enter a decimal number: "))

integer_num = int(decimal_num)
string_num = str(decimal_num)

print("Original Decimal:", decimal_num)
print("Integer Value:", integer_num)
print("String Value:", string_num)


age = input("Enter your age: ")

print("Age entered:", age)
print("Data type:", type(age))

age = int(age)

print("Age after conversion:", age)
print("Data type after conversion:", type(age))


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Modulus =", num1 % num2)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Equal to:", num1 == num2)
print("Not equal to:", num1 != num2)


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
  print("Login Successful")
else:
  print("Login Failed")


num = float(input("Enter a number: "))

if num > 0:
 print("Positive")
elif num < 0:
 print("Negative")
else:
 print("Zero")


marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


choice = int(input("Enter your choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", num1 + num2)
elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
elif choice == 4:
    print("Result =", num1 / num2)
else:
    print("Invalid Choice")


for i in range(1,21):
    print(i)


for i in range(2, 51, 2):
    print(i)


num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


i = 10

while i >= 1:
    print(i)
    i -= 1


total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


num = int(input("Enter a number: "))

count = 0

while num != 0:
    num = num // 10
    count += 1

print("Number of digits =", count)


for i in range(1, 21):
    if i == 15:
        break
    print(i)


for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Correct Password")
        break
    else:
        print("Try Again")


        for i in range(1, 6):
            print("*" * i)


for i in range(1, 6):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()


for i in range(1, 5):
    for j in range(4):
        print(i, end="")
    print()


students = ["Aarohi", "Rahul", "Sneha", "Amit", "Priya"]

print("First student:", students[0])
print("Last student:", students[-1])
print("Total number of students:", len(students))


numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("List:", numbers)


numbers = [30, 10, 50, 20]

numbers.append(40)
print("After append:", numbers)

numbers.remove(10)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)


numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)


numbers = [10, 25, 5, 40, 15]

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of all elements:", sum(numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 elements:", numbers[:5])
print("Last 3 elements:", numbers[-3:])
print("Alternate elements:", numbers[::2])


details = ("Aarohi", 20, "Pune")

print("Name:", details[0])
print("Age:", details[1])
print("City:", details[2])


student = ["Aarohi", 20, "Pune"]

student[1] = 21

print(student)


numbers = (10, 25, 5, 40, 15)

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Total sum:", sum(numbers))


student = ("Aarohi", 20, "Pune")

name, age, city = student

print("Name:", name)
print("Age:", age)
print("City:", city)


balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance =", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Updated Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")


marks = []

for i in range(5):
    mark = float(input("Enter marks of subject " + str(i + 1) + ": "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Marks:", marks)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

print("Highest Marks:", max(marks))
