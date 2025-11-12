# 1. Basic List Operations

# Q1: Create a list of the first 10 natural numbers and print the list.
 
# natural_number = []
# for i in range(1,11):
# natural_number.append(i)
# print(natural_number)

# natural_numbers = list(range(1, 11))
# print(natural_numbers)

# Q2: Access and print the 4th element in the list of natural numbers.

# list = [1, 2, 3, 4, 5,]
# print(list[3])

# Q3: Print the last element using negative indexing from the list of natural numbers.

# natural_number = []
# for i in range(1,11):
#     natural_number.append(i)
# print( natural_number[: -2: -1])

# Q4: Change the 2nd element of the list to 100 and print the updated list.

# number = []
# for i in range(1,5):
#     number.append(i)
# number[1] = 100
# print(number)

# 2. List Slicing

# Q5: Create a list of numbers from 1 to 20. Use slicing to extract the first 5 elements and print them.

# list = []

# for i in range(1, 21):
#     list.append(i)
# print(list[:5])

# Q6: From the list of numbers 1 to 20, extract and print all elements from index 10 to the end.

# list = []

# for i in range(1, 21):
#     list.append(i)
# print(list[10:]) 


# Q7: From the list of numbers 1 to 20, extract and print every other element (use step size in slicing).

# list = []

# for i in range(1, 21):
#     list.append(i)

# Q8: Create a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Print all elements except the first one using slicing.

# list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# print(list[2:])

# 3. List Modifications

# Q9: Add a new element to the end of the list using append(). (Try with a number or string).

# list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# list.append("kay vachtoy lavdya")
# print(list)

# Q10: Insert a number 99 at index 3 in the list [1, 2, 3, 4, 5] using insert(). Print the updated list.

# list = []
# for i in range(0,5):
#     list.append(i)
# print(list)
# list[2] = 99
# print(list)


# Q11: Remove the last element from the list using pop(). Print the updated list.

# list = []
# for i in range(0,5):
#     list.append(i)
# print(list)
# list.pop[::-1]
# print(list)

# Q12: Remove the element 3 from the list using remove(). Print the list after removal.

# list = []
# for i in range(0,5):
#     list.append(i)
# print(list)
# list.remove(3)
# print(list)

# Q13: Use extend() to add a list [10, 20, 30] to the end of the list [1, 2, 3]. Print the updated list.

# list = [1, 2, 3]
# list.extend([10, 20, 30])
# print(list)


# 4. List Methods & Functions

# Q14: Sort a list of numbers [23, 1, 34, 12, 5] in ascending order using sort(). Print the sorted list.

# list = [23, 1, 34, 12, 5]
# list.sort()
# print(list)

# Q15: Sort the list of strings ['apple', 'banana', 'cherry', 'date'] in reverse alphabetical order using sort(reverse=True).

# list = ['apple', 'banana', 'cherry', 'date']
# list.sort(reverse=True)
# print(list)


# Q16: Use reverse() to reverse the order of elements in the list [10, 20, 30, 40, 50] and print the result.

# list = [10, 20, 30, 40, 50]
# list.reverse()
# print(list)

# Q17: Find and print the index of the element 40 in the list [10, 20, 30, 40, 50] using index().

# list = [10, 20, 30, 40, 50]
# print(list.index(40))

# 5. List Comprehensions

# Q18: Use a list comprehension to create a list of the first 10 square numbers (e.g., 1, 4, 9, ..., 100).

# list = [i * i  for i in range (11) ]
# print(list)

# for i in range (1,10+1):
#     list.append(i*i)
# print(list)


# Q19: Create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.

# list = [ i for i in range (1, 50) if i % 5 == 0]
# print(list)


# list = []
# for i in range(1, 50):
#     if i%5==0:
#         list.append(i)
# print(list)

# Q20: Create a list of strings where each string is the name of a fruit in uppercase (e.g., "APPLE", "BANANA") using list comprehension.

# fruits = ["apple", "banana"]
# uppercase_fruits = [fruit.upper() for fruit in fruits]

# print(uppercase_fruits)


# 6. Nested Lists and Loops
# Q21: Create a list of lists representing a 3x3 matrix (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Access and print the element in the 2nd row, 3rd column.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)

# Q22: Create a list of numbers from 1 to 5 and use a for loop to print each element and its square (e.g., 1, 1, 2, 4).

# for i in range(1, 5+1):
#     print(i, " square is " , i*i)

# Q23: Create a 2D list of numbers and use nested loops to print all elements in the 2D list one by one.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)

# for row in matrix:
#     for element in row:
#         print(element)


# 7. List Operations and Efficiency

# Q24: Create two lists: list1 = [1, 2, 3] and list2 = [4, 5, 6]. Concatenate them into one list using the + operator and print the result.

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concat_list = list1 + list2
# print(concat_list)

# Q25: Repeat the list [1, 2, 3] three times using the * operator and print the result.

# list = [i for i in range(1, 4)]
# print(list * 3)

# Q26: Given a list [1, 2, 3, 4, 5], use pop() to remove the 2nd element (index 1) and print the updated list.

# list = [1, 2, 3, 4, 5]
# list.pop(1)
# print(list)

# Q27: Given the list [10, 20, 30, 40, 50], remove all even numbers using a list comprehension.

# list = [i*10 for i in range(1,6) ]
# list = [num for num in list if num % 2 != 0]
# print(list)

# 8. Advanced List Manipulations

# Q28: Check if a number 50 exists in the list [10, 20, 30, 40, 50]. Use the in operator and print True or False.

# list = [10, 20, 30, 40, 50]
# if 50 in list: 
#     print("true")

# Q29: Given a list of strings ['apple', 'banana', 'cherry', 'date'], create a new list containing only those strings that contain the letter "a".

# fruits = ['apple', 'banana', 'cherry', 'date']
# a_present = [fruit for fruit in fruits if 'a' in fruit]
# print(a_present)

# Q30: Create a list of the first 10 Fibonacci numbers using a for loop and store them in a list.
# n = 10
# a = 0
# b = 1
# fibonacci = [] 
# for _ in range(n):
#     fibonacci.append(a)
#     a , b = b , a + b
# print(fibonacci)


# 9. Additional Practice with List Functions

# Q31: Find and print the sum of all numbers in a list [5, 10, 15, 20] using sum().

# list = [i * 5 for i in range(1 , 5)]
# t = sum(list)
# print(t)

# Q32: Use the max() and min() functions to find the largest and smallest numbers in the list [100, 25, 75, 50].

# list  = [100, 25, 75, 50]
# print(min(list))
# print(max(list))

# Q33: Use len() to find the length of the list ['apple', 'banana', 'cherry', 'date'] and print the result.

# list = ['apple', 'banana', 'cherry', 'date']
# print(len(list))

# Q34: Use all() to check if all numbers in the list [1, 2, 3, 4] are positive.

# list = [i for i in range(1 , 5)]
# if all(num > 0 for num in list):
#     print("All numbers are positive")
# else:
#     print("Not all numbers are positive")

# Q35: Use any() to check if any number in the list [-1, 2, 3, 4] is negative.

# list = [-1, 2, 3, 4]
# if any (num < 0 for num in list):
#     print("there is a negative number ")
# else:
#     print("there is no negative number present")

# 10. Working with Lists and Conditionals

# Q36: Create a list of numbers from 1 to 20. Use a list comprehension to create a new list containing only the even numbers from the original list.

# list = [i for i in range(1, 21)]
# new = [num for num in list if num % 2 == 0]
# print(list)
# print(new)

# Q37: Write a program that creates a list of numbers from 1 to 30, and then use filter() to create a new list of numbers greater than 15.

# my_list = [i for i in range(1, 30)]
# print(my_list)
# new_list = list(filter(lambda x: x > 15, my_list))
# print(new_list)


# Q38: Write a function that takes a list and a number, and returns a new list where the number is added at the end only if it is not already in the list.

# num1 = [2, 4, 8, 7, 9, 5, 3, 1, 0]
# # print(num1.index(4))

# val = int(input("ENter the value which u want to add "))

# if val not in num1:
#     num1.append(val)
#     print(num1)
# else:
#     print("Value exists in the list already")

# 1. Basic Tuple Operations

# Q1: Create a tuple fruits with the following elements: "apple", "banana", "cherry". Print the entire tuple.

# fruits = ("apple", "banana", "cherry")
# print(fruits)

# Q2: Create a tuple numbers with 5 elements: 10, 20, 30, 40, 50. Access and print the third element (index 2).

# numbers = 10, 20, 30, 40, 50
# print(numbers[2])
# print(type(numbers))    

# Q3: Create a tuple colors with the elements "red", "green", and "blue". Change the value of the second element to "yellow". (Is it possible? Explain why or why not.) no lavdyaaaaaa they are immutable

# colors = ("red", "green", "blue")
# colors. = "yellow"

# 2. Slicing and Indexing

# Q4: Create a tuple animals with the following elements: "dog", "cat", "elephant", "giraffe", "rabbit". Print a slice of the first 3 animals.

# animals =  ("dog", "cat", "elephant", "giraffe", "rabbit")
# print(animals[0:3])

# Q5: Create a tuple days containing all days of the week. Print the last 3 days using slicing.

# all_days = ("monday", "tuesday", "wednesday", "thurday", "friday", "saturday", "sunday")
# print(all_days[4:])

# Q6: Create a tuple numbers with elements from 1 to 10. Print every other element using slicing (e.g., print elements at index 0, 2, 4, etc.).

# number = tuple(range(1,11))
# print(number[1::2])

# 3. Tuple Unpacking

# Q7: Given a tuple person = ("John", 30, "Engineer"), unpack it into individual variables and print them (i.e., name, age, and profession).

# person = ("John", 30, "Engineer")
# x = (person[0])
# y = (person[1])
# z = (person[2])
# print (x)
# print (y) 
# print(z)

# Q8: Given a tuple coordinates = (5, 10, 15), unpack it into variables x, y, and z. Then, print the sum of these coordinates.

# coordinates = (5, 10, 15 )
# x = (coordinates[0])
# y = (coordinates[1])
# z = (coordinates[2])

# sum = x + y + z
# print(sum)

# Q9: Create a tuple student_info = ("Alice", "A", 18) and use unpacking to assign the elements to variables: name, grade, and age.

# student_info =  ("Alice", "A", 18)
# name = student_info[0]
# grade = student_info[1]
# age = student_info[2]
# print (f"Name is {name} his grade is {grade} and age is {age} ")

# 4. Tuple Operations (Concatenation, Repetition, etc.)

# Q10: Concatenate two tuples a = (1, 2, 3) and b = (4, 5, 6) and print the resulting tuple.

# a = (1, 2, 3) 
# b = (4, 5, 6)
# c = a + b 
# print(c)

# Q11: Create a tuple letters = ('a', 'b', 'c') and repeat it 3 times. Print the result.

# letters =  ('a', 'b', 'c')
# x = (letters * 3)
# print(x)

# Q12: Given a tuple numbers = (10, 20, 30, 40), check if the number 30 exists in the tuple. Print True or False.

# numbers = (10,20,30,40)
# if 30 in numbers :
#     print ("true")
# else :
#     print("false")

# 5. Nested Tuples

# Q13: Create a nested tuple data = (("John", 25), ("Alice", 30), ("Bob", 22)). Print the second element of the second tuple (i.e., Alice’s age).

# data = (("John", 25), ("Alice", 30), ("Bob", 22))
# print(data[1][1])

# Q14: Create a tuple nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9)). Access and print the value 5 using indexing.

# nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# x = nested[1][1]
# print(x)

# Q15: Given a tuple of tuples matrix = ((1, 2), (3, 4), (5, 6)), print the sum of the elements in the second tuple.

# matrix = ((1, 2), (3, 4), (5, 6))
# x = sum(matrix[1])
# print(x)

# 6. Tuple Length and Count

# Q16: Create a tuple fruits = ("apple", "banana", "cherry", "apple"). Find and print the length of the tuple.

# fruits = ("apple", "banana", "cherry", "apple")
# x = len(fruits)
# print(x)

# Q17: Create a tuple nums = (1, 2, 3, 4, 1, 1). Count how many times the number 1 appears in the tuple and print the result.

# nums = (1, 2, 3, 4, 1, 1)
# print(nums.count(1))

# Q18: Given a tuple t = ("hello", "world", "python", "hello"), print how many times the string "hello" appears in the tuple.

# 7. Immutability of Tuples

# Q19: Create a tuple t = (1, 2, 3, 4). Try to change the second element to 5 and explain the error.

# t = (1, 2, 3, 4)
# t([1]) = 5
# print(t) cannot assign the value to tuple it is immutable

# Q20: Create a tuple names = ("Alice", "Bob", "Charlie"). Try to append a new element "David" to the tuple and explain the error.

# names = ("Alice", "Bob", "Charlie")
# names.append("David") (The .append() method is available only for lists, not tuples. Tuples are immutable, meaning you cannot add, remove, or modify elements once they’re created.

# Q21: Create a tuple numbers = (1, 2, 3, 4). Convert this tuple to a list, add a new number 5, and then convert it back to a tuple. Print the modified tuple.

# numbers = (1, 2, 3, 4)
# x = list(numbers)
# x.append(5)
# print(x)
# numbers = tuple(x) 
# print(numbers)

# 8. Tuple as Dictionary Keys

# Q22: Create a tuple point = (2, 3). Use this tuple as a key in a dictionary with the value "Location A". Print the dictionary.

# point = (2, 3)
# dict = {(point) :"Location A" }
# print(dict)

# Q23: Create a dictionary with tuples as keys:
# d = {("apple", "banana"): "fruit", ("carrot", "potato"): "vegetable"}.
# Retrieve and print the value for the key ("apple", "banana").

# d = {("apple", "banana"): "fruit", ("carrot", "potato"): "vegetable"}
# print(d["apple", "banana"])

# 9. Working with Multiple Tuples

# Q24: Create two tuples a = (1, 2, 3) and b = (4, 5, 6). Swap the values between a and b using tuple unpacking.

# a = (1, 2, 3)
# b = (4, 5, 6)
# a, b = b, a
# print(a)
# print(b)

# Q25: Given a tuple of tuples data = ((1, 2), (3, 4), (5, 6)), add the elements from the second tuple to the first tuple. Print the result.

# data = ((1, 2), (3, 4), (5, 6))
# x = data[0]+ data[1]
# print(x)

# 10. Advanced Operations

# Q26: Create a tuple numbers = (5, 10, 15, 20, 25). Use a list comprehension to create a new tuple that contains only the numbers greater than 10.

# numbers = (5, 10, 15, 20, 25)
# greaterthan10 = tuple(x for x in numbers if x > 10)
# print(greaterthan10)  

# Q27: Create a tuple numbers = (3, 6, 9, 12, 15). Use a loop to iterate through the tuple and print each element squared.

# numbers = (3, 6, 9, 12, 15)
# square = tuple(x**2 for x in numbers)
# print(square)

# 🟢 EASY LEVEL (Basics)

# Create a dictionary of  3 students with their marks and print all keys and values separately.

# avd = {
#     "prasad" : 92 ,
#     "roshan" : 82 ,
#     "pushpak" : 80 ,
#     "om" : 90 , 
#     "vinayak" : 95
# }
# keys = avd.keys()
# values = avd.values()
# print(f"keys : {keys}" )
# print(f"values : {values}")

# Add a new key–value pair to an existing dictionary.

# avd = {
#     "prasad" : 92 ,
#     "roshan" : 82 ,
#     "pushpak" : 80 ,
#     "om" : 90 , 
#     "vinayak" : 95
# }
# avd ["vivek"] : 88
# print(avd)

# Check if a given key exists in a dictionary.

# x = str(input("enter the key : "))
# avd = {"prasad" : 92 , "roshan" : 82 ,"pushpak" : 80 ,"om" : 90 , "vinayak" : 95 }
# if x in avd :
#     print("present")
# else :
#     print("not present")

# Safely remove a key using .pop() or .pop(key, default) (no error if missing).

# avd = {"prasad" : 92 , "roshan" : 82 ,"pushpak" : 80 ,"om" : 90 , "vinayak" : 95 }
# avd.pop("pushpak", None)
# print(avd)

# Get a value using .get() and return "Not Found" if the key doesn’t exist.

# avd = {"prasad" : 92 , "roshan" : 82 ,"pushpak" : 80 ,"om" : 90 , "vinayak" : 95 }
 
# value = avd.get("pushpak","not present")
# print(value)

# Find the length of a dictionary using len().

# avd = {"prasad" : 92 , "roshan" : 82 ,"pushpak" : 80 ,"om" : 90 , "vinayak" : 95 }
# x = len(avd)
# print(x)

# Convert two lists → one dictionary (keys list + values list).

# keys = ["roshan", "om", "vinayak", "prasad"]
# values = [94 ,90, 98 ,69]
# x = dict(zip(keys, values))
# print(x)

# Copy one dictionary into another using .copy().

# avd = {"prasad" : 92 , "roshan" : 82 ,"pushpak" : 80 ,"om" : 90 , "vinayak" : 95 }
# x =  avd.copy()
# print(x)

# Create a dictionary where keys = numbers (1–5) and values = their squares.

# numbers = {}            
# for i in range(1, 6):    
#     numbers[i] = i * i
# print(numbers)

# Merge two dictionaries into one (without duplicates overwriting)

# dict1 = {}
# dict2 = {}
# for i in range(6):
#     dict1[i] = i 
#     dict2[i] = i*i
# x = list(zip(dict2,dict1))
# print(x)

# 🟡 MEDIUM LEVEL (Loops & Operations)

# Count the frequency of each character in a string using a dictionary.

# text = input("Enter a string: ")
# freq = {}
# for ch in text:
#     if ch in freq:
#         freq[ch] = freq[ch] + 1
#     else:
#         freq[ch] = 1
# print("Character frequencies:")
# print(freq)


# Print only those keys whose values are greater than a given number (like > 50).

# shamnya = {
#     "Alice": 45,
#     "Bob": 72,
#     "Charlie": 68,
#     "David": 50,
#     "Eve": 91,
#     "Frank": 33,
#     "Grace": 77
# }

# for name in shamnya.keys():
#     if shamnya[name] > 50:
#         print(name, shamnya[name])

# Check if a given value exists in the dictionary (not key).
new = {
    "Alice": 45,
    "Bob": 72,
    "Charlie": 68,
    "David": 50,
    "Eve": 91,
    "Frank": 33,
    "Grace": 77
}

x = input(" enter the keys or values to check in dictonary : ")
for name,values in new.items():
    if name == new.keys():
        print(f"this {keys} key is  present in dict")
    if values == new.values():
        print(f"this {}"
# Sort a dictionary by its keys (ascending & descending).

# Sort a dictionary by its values.

# Calculate the sum of all values in the dictionary.

# Find the key with the maximum and minimum value.

# Remove all keys that have None, "", or empty values.

# Swap keys and values in a dictionary (only if values are unique).

# Double each dictionary value using a loop or comprehension.

# 🔵 ADVANCED LEVEL (Nested + Comprehension)

# Given:

# students = {
#     "101": {"name": "Roshan", "marks": 80},
#     "102": {"name": "Om", "marks": 90}
# }


# Print all student names and marks.
# 22. Add a new student entry dynamically to the above nested dictionary.
# 23. Extract all student names into a list using a loop or list comprehension.
# 24. Write a dictionary comprehension for numbers and their cubes (1–10).
# 25. Merge two dictionaries but if a key repeats, add their values.
# 26. Invert a dictionary (swap keys ↔ values), only for unique values.
# 27. From d = {'a':[1,2], 'b':[3,4]}, create → [('a',1),('a',2),('b',3),('b',4)].
# 28. Count how many times each word appears in a sentence using a dictionary.
# 29. Given a nested dictionary of employees with their salaries, calculate the total salary.
# 30. Flatten a nested dictionary into a single-level dictionary (e.g. "emp.details.name" style keys).

# 🟢 EASY (1–5)

# Write a function that takes a list of numbers and returns the sum of all even numbers.

# list = [1,2,3,4,5]

# def sum_of_list(nums):
#     total = 0 
#     for i in nums:
#         if i % 2 == 0:
#             total += i
#     return total

# print(sum_of_list(list))
    
# Write a function to count how many vowels are in a given string.

# def checker(str):
#     vowels = "aeiou"
#     count = 0
#     for char in vowels:
#         if char in x:
#             count += 1
#     return count
# x = input("enter the string : ") 
# u = checker(x)
# print(u)


# Write a function that takes a list of numbers and returns a list of squares of each number.
    
# def squares_list(nums):
#     result = []
#     for n in nums:
#         result.append(n ** 2)
#     return result

# numbers = [1, 2, 3, 4, 5]
# print(squares_list(numbers)) 

# Write a function that takes a string and returns the reversed string using a loop.

# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s   
#     print("Reversed string:", reversed_s)  
#     return reversed_s

# x = input("Enter the string to reverse: ")
# reverse_string(x)

# Write a function that takes a number n and prints the first n multiples of 3 using a loop.

# x = input("enter the number : ")
# for i in range(x):
#     if i % 3 == 0:
#         print

# 🟡 MEDIUM (6–10)

# Write a function to count the frequency of each character in a string and return a dictionary.

# Write a function that takes a list of numbers and returns only the prime numbers in a new list.

# x = int(input("Enter the number to check if it is prime or not: "))

# if x > 1:
#     for i in range(2, x):
#         if x % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not prime")

# Write a function that takes a nested list (like [[1,2],[3,4],[5]]) and returns a flattened list.



# Write a function that takes a string and returns the longest word in it using a loop.

# Write a function that prints a triangle pattern of stars for a given number n (usig nested loops).

# 🔵 HARD (11–15)

# Write a function that takes a number n and returns a list of factorials from 1 to n.

# Write a function that takes a list of strings and returns only the palindromes.

# Write a function that takes a nested dictionary of students (with marks) and returns the student with highest marks.

# Write a function to merge two lists element-wise and return a list of sums. Example: [1,2,3] & [4,5,6] → [5,7,9].

# Write a function that prints a pyramid number pattern for given n using nested loops. Example for n=3:

#   1
#  2 3
# 4 5 6


# input/output

# 1. Read and Print a File
# m = open("br.txt","r")
# data = m.read()
# print(data)
# m.close

# m = open("br.txt","a+")
# data = m.write("wasssup bitches")
# m.seek(0)
# print(m.read())
# m.close

# 2. Count Lines in a File

# file = open("br.txt","r")
# lines = file.readlines()
# print(lines,len(lines))

# Create a file sample.txt and read its entire content

# file = open("gandu.txt","w+")
# data = file.write("chinaal kashi yes")
# file.seek(0)
# print(file.read())

# Read only the first 10 characters of a file.

# file = open("gandu.txt","w+")
# data = file.write("chinaal kashi yes")
# file.seek(0)

# Read a file line by line using both readline() and readlines().

# Write 3 lines of text into output.txt and verify its contents.

# Append "New Data Added" to an existing file and print the updated content.

# Write a list of strings ["Apple", "Banana", "Cherry"] to a file, each on a new line.

# Open a file, read the first 5 characters, print the cursor position, reset it, and read again.

# Use with statement to read a file and print whether the file is closed inside and outside the block.

# Handle the case when a file does not exist; if it does, print content; else, print "File not found!".

# Read a file data.txt, count the frequency of each word, and write the results into count.txt.