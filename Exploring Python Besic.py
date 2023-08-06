#Task 1: variable manipulation
def task1():
    name = "Nawaz Sharif"
    age = 25
    print("My name" + name + "and I am + str(age)")

#Task 2: Data Types and Type Conversion
def task2():
    num1 = 10
    num2 = 10.5
    num1_int = int(num1)
    num2_float = float(num2)
    print("num1:" + str(num1))
    print("num1_int:" + str(num1_int))
    print("num1:" + str(num1))
    print("num2_float:" + str(num2_float))

#Task 3: String Manipulation
def task3():
    sentence = "Python programming is fun!"
    print("Length of" + sentence + "is:" + str(len(sentence)))
    print("8th character of" + sentence + "is:" + str(sentence[7]))
    substring = sentence[:6]
    print("I enjoy it!" + substring)

#Task 4: Lists and List Manipulation
def task4():
    fruits = ["apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print(len(fruits))
    sliced_fruits = fruits[2:4]
    print(sliced_fruits)
    extra_fruits = ["Kiwi", "lemon"]
    combined_fruits = sliced_fruits + extra_fruits
    print(combined_fruits)

#Task 5: Conditional Statements
num = int(input("Enter the value:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Task 6: Loops
for num in range(1,11):
    print(num)
    sum = 0
for num in range(1,101):
    sum = sum + sum
    print(sum)

#Task 7: Functions
def calculate_square(num):
    return num * num
def is_prime (num):
    flag = True
for n in range(2,num):
    if num % n == 0:
        flag = False
    break; 
    return flag
print(is_prime (11))

#Task 8: Dictionaries
def calculate_square(num):
    return num * num
def is_prime (num):
    flag = True
for n in range(2,num):
    if num % n == 0:
        flag = False
    break; 
    return flag 
print(calculate_square(7))
print(is_prime (11))

#Task 8: Dictionaries
student = "name:" + "Nawaz Sharif", + "age:" + "25", + "grade:" + "A+"
student["course"] = "Web Engineering"
print("Keys in the dictionary:")
for key in student.keys():
    print(key)
print("Key-Value pairs in the dictionary:")
for key, value in student.items():
    print(key, ":",value)