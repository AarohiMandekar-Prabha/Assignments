# Q1
student = {
    "name": "aarohi",
    "age": 19,
    "course": "AIML",
    "city": "Pune"
}

print(student)

print()


# Q2
employee = {
    "name": "Rahul",
    "salary": 50000,
    "department": "IT"
}

print("Employee Name =", employee["name"])
print("Salary =", employee["salary"])
print("Department =", employee["department"])

print()


# Q3
student["email"] = "aarohi.mandekar.prabha@gmail.com"

print(student)

print()


# Q4
student["city"] = "Mumbai"

print(student)

print()


# Q5
student.pop("email")
print(student)

del student["course"]
print(student)

print()


# Q6
student = {
    "name": "aarohi",
    "age": 19,
    "course": "AIML",
    "city": "Pune"
}

print("Keys:")
for key in student.keys():
    print(key)

print()

print("Values:")
for value in student.values():
    print(value)

print()

print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

print()


# Q7
marks = {
    "Math": 85,
    "Science": 90,
    "English": 80,
    "Python": 95
}

print("Total Subjects =", len(marks))

print()


# Q8
marks = {
    "Math": 85,
    "Science": 90,
    "English": 80,
    "Python": 95,
    "AI": 88
}

total = sum(marks.values())

print("Total Marks =", total)

print()


# Q9
key = input("Enter key to search: ")

if key in student:
    print("Key Exists")
else:
    print("Key Not Found")

print()


# Q10
products = {
    "Laptop": 55000,
    "Mouse": 700,
    "Keyboard": 1200,
    "Pen": 20,
    "Bag": 800
}

print("Products with price greater than 500:")

for product, price in products.items():
    if price > 500:
        print(product, "=", price)


# Q11
numbers = {10, 20, 30, 40, 50}

print("Set Elements:")
for num in numbers:
    print(num)

print()


# Q12
numbers.add(60)
numbers.add(70)

print("After Adding Elements:")
print(numbers)

print()


# Q13
numbers.remove(20)
print("After remove():", numbers)

numbers.discard(70)
print("After discard():", numbers)

print()


# Q14
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union =", set1 | set2)
print("Intersection =", set1 & set2)
print("Difference =", set1 - set2)

print()


# Q15
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Common Elements =", set1.intersection(set2))

print()


# Q16
value = int(input("Enter a number: "))

if value in set1:
    print("Value Exists")
else:
    print("Value Not Found")

print()


# Q17
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print("Set =", unique_numbers)

print()


# Q18
students = {"aarohi", "Rahul", "Amit", "anushka", "Priya"}

print("Unique Students =", students)
print("Total Unique Students =", len(students))

print()


# Q19
set1 = {1, 2, 3}
set2 = {1, 2, 3}

if set1 == set2:
    print("Both Sets are Equal")
else:
    print("Both Sets are Not Equal")

print()


# Q20
set1.clear()

print("After Clear =", set1)


# Q21
def welcome():
    print("Welcome to Python Programming")

welcome()

print()


# Q22
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

print()


# Q23
def greet(name):
    print("Hello,", name)

greet("Rohit")

print()


# Q24
def square(num):
    print("Square =", num * num)

square(5)

print()


# Q25
def even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

even_odd(8)

print()


# Q26
def area(length, width):
    print("Area =", length * width)

area(10, 5)

print()


# Q27
def greater(a, b):
    if a > b:
        return a
    else:
        return b

print("Greater Number =", greater(15, 20))

print()


# Q28
def numbers():
    for i in range(1, 11):
        print(i)

numbers()

print()


# Q29
def total(numbers):
    return sum(numbers)

num_list = [10, 20, 30, 40, 50]

print("Sum =", total(num_list))

print()


# Q30
def result(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")

result(45)

print()


# Q31
def student(name, city="Pune"):
    print("Name =", name)
    print("City =", city)

student("Soham")

print()


# Q32
def details(name, age):
    print("Name =", name)
    print("Age =", age)

details(age=19, name="aarohi")

print()


# Q33
def values(*numbers):
    for num in numbers:
        print(num)

values(10, 20, 30, 40, 50)

print()


# Q34
def maximum_minimum(numbers):
    return max(numbers), min(numbers)

num_list = [25, 50, 10, 90, 60]

maximum, minimum = maximum_minimum(num_list)

print("Maximum =", maximum)
print("Minimum =", minimum)

print()


# Q35
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count

word = input("Enter a string: ")

print("Total Vowels =", count_vowels(word))


