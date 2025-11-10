# 1 Write a Python program to add two numbers entered by the user

# a = int(input("enter the first number : "))
# b = int(input("enter the second numer : "))

# c = (a + b)
# print(c)

# 2 Write a Python program to subtract two integers entered by the user.

# a = int(input("enter the first number : "))
# b = int(input("enter the second numer : "))

# c = (a - b)
# print(c)

# 3 Write a Python program to multiply two floating-point numbers.

# a = float(input("Enter the first float to multiple : "))
# b = float(input("Enter the second floa to multiple : "))
# c = (a * b)
# print(c)

# 4 Write a program to divide two numbers and display the quotient.

# a = int(input("Enter the divident : "))
# b = int(input("Enter the divisor : "))
# c = (a / b)
# print(c)

# 5 Write a program to find the remainder when one number is divided by another.

# num1 = int(input("Enter the first number (dividend): "))
# num2 = int(input("Enter the second number (divisor): "))

# if num2 == 0:
#     print("Error: Division by zero is not allowed.")
# else:
#     remainder = num1 % num2
#     print(f"The remainder when {num1} is divided by {num2} is: {remainder}")

# 6 Program to find the remainder when one number is divided by another

# numerator = int(input("numerator : "))
# denominator = int(input("denominator : "))

# remainder = numerator % denominator

# print(f"The remainder when {numerator} is divided by {denominator} is: {remainder}")

# 7 Program to find the remainder when one number is divided by another

# numerator = int(input("Enter the numerator: "))
# denominator = int(input("Enter the denominator: "))

# if denominator == 0:
#     print("Error: Division by zero is not allowed.")
# else:
#     remainder = numerator % denominator
#     print("The remainder is:", remainder)

# 8 Write a program to find both the quotient and remainder for two integers.
 
# numerator = int(input("Enter the numerator: "))
# denominator = int(input("Enter the denominator: "))

# if denominator == 0:
#     print("Error: Division by zero is not allowed.")
# else:
#     quotient = numerator // denominator    # Integer division
#     remainder = numerator % denominator    # Modulo (remainder)
    
#     print("Quotient:", quotient)
#     print("Remainder:", remainder)

# 9 Write a program to calculate the square of a number using the exponent operator.

# a = int(input("enter the number : "))

# b = (a**2)
# print("square of ", a , "is ", b)

#  Write a program to calculate the cube of a number.

# a = int(input("enter the number : "))

# b = (a**3)
# print("cube of ", a , "is ", b)

# 10 Write a program to add three numbers entered by the user.

# a = int(input("first number : "))
# b = int(input("second number : "))
# c = int(input("third number : "))

# d = (a + b + c)
# print("total sum ",d)

# 11 Write a program to perform all arithmetic operations on two numbers.

# a = int(input("first number : "))
# b = int(input("second number : "))
# print("addition : ", a + b)
# print("subtraction : ", a - b)
# print("multiplication : ", a * b )
# print("division : ", a / b)

# 12 Write a program to find the average of two numbers.

# a = int(input("first number : "))
# b = int(input("second number : "))
# average = (a+b)/2
# print(average)

# 13 Write a program that reads two numbers and prints their sum and difference.

# a = int(input("first number : "))
# b = int(input("second number : "))
# print("sum : ", a + b)
# print("difference : ", a - b)

# 14 Write a program to compute 10 + 5 * 2 and show how operator precedence works.

# result1 = 10 + 5 * 2
# result2 = (10 + 5) * 2

# print("Result of 10 + 5 * 2 =", result1)
# print("Result of (10 + 5) * 2 =", result2)

#15 Write a program to demonstrate the difference between / and // operators.

# a = float(input(" divident : "))
# b = float(input(" divisor : "))

# c = (a/b)
# d = (a//b)
# print("result of /   :",c)
# print("result of //  : ",d)


# 16 Write a program that takes two numbers and displays (a + b)**2 and (a - b)**2.

# a = float(input("first number : "))
# b = float(input("second number : "))

# c = (a + b)**2 
# d = (a - b)**2

# print("result of (a + b)**2 :",c)
# print("result of (a - b)**2 : ",d)

# 17 Write a program to convert a total number of minutes into hours and minutes using // and %.

# total_minutes = int(input("total number of minutes: "))

# hours = total_minutes // 60
# # minutes = total_minutes % 60

# print(f"{total_minutes} minutes is equal to {hours} hour(s) and {minutes} minute(s).")

#118 Write a program to find the area of a rectangle using arithmetic operators.

# a = float(input("length : "))
# b = float(input("breath : "))
# c = (a * b)
# print (f"area of rectangle : ",c)

# 19 Write a program to find the perimeter of a triangle using arithmetic operators.

# a = int(input("first side : "))
# b = int(input("second side : "))
# c = int(input("third side : "))
# perimeter = (a + b + c)
# print(perimeter)

# 20 Write a program to calculate the simple interest using the formula SI = (P * R * T) / 100.

# P =  float(input("principal investment amount : "))
# R = float(input("annual interest rate : "))
# T =  float(input("number of years the money is invested or borrowed : "))
# SI = (P * R * T) / 100.
# print("Simple interest is ", SI)

# 21 Write a program to calculate the compound interest using arithmetic operations.

# P =  float(input("principal investment amount : "))
# r = float(input("annual interest rate in decimal form : "))
# n =  float(input("number of times that interest is compounded per year : "))
# t =  float(input("number of years the money is invested or borrowed : "))
# compound_interest = P * (1 + r / n) ** (n * t)

# print(compound_interest)

# 22 Write a program to find the average marks of 5 subjects and print total and percentage.

# a = float(input("first number : "))
# b = float(input("second number : "))
# c = float(input("third number : "))
# d = float(input("fourth number : "))
# e = float(input("fifth number : "))

# average = float(a + b + c + d + e)/5
# print("average of all five subjects : ", average)

# 23 Write a program to find the area and circumference of a circle.
# r = float(input("radius : "))
# area = ( 3.14 * r**2 )
# circumference = (2 * 3.14 * r )
# print("area of circle : ", area)
# print("circumference : ", circumference)

# 24 Write a program to swap two numbers without using a third variable (using + and -).

# a = int(input(" first number : "))
# b = int(input(" second number : "))

# print(f"Before swapping: a = {a}, b = {b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"After swapping: a = {a}, b = {b}")

# 25 Write a program to calculate the BMI (Body Mass Index) of a person using formula BMI = weight / (height ** 2).

# weight = float(input("weight in kg : "))
# height = float(input("height in cm : "))
# BMI = weight / (height ** 2)

# print(BMI)

# 26 Write a program to find the area of a triangle using Heron’s formula.

# a = int(input("First side: "))
# b = int(input("Second side: "))
# c = int(input("Third side: "))
# semiperimeter = (a + b + c) / 2
# area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)) ** 0.5

# print("Semiperimeter:", semiperimeter)
# print("Area by Heron's formula:", area)

#27 Write a program to calculate the total salary given basic, HRA (10%), and DA (5%).

# basic = float(input("Enter basic salary: "))

# hra = 0.10 * basic
# da = 0.05 * basic

# total_salary = basic + hra + da

# print("HRA (10%):", hra)
# print("DA (5%):", da)
# print("Total Salary:", total_salary)

# 28 Write a program to calculate the final price after a discount percentage is applied.

# price = float(input("Enter the price: "))
# discount_percentage = float(input("Enter the discount %: "))

# discount_amount = (discount_percentage / 100) * price
# after_discount_price = price - discount_amount

# print("After discount price:", after_discount_price)

# 29 Write a program to convert Celsius temperature to Fahrenheit.

# celsius = float(input(" enter the celsius : "))
# Fahrenheit = (celsius * (9/5)) + 32 
# print(Fahrenheit)

#30  Write a program to convert Fahrenheit to Celsius.

# Fahrenheit = float(input(" enter the Fahrenheit : "))
# celsius = (Fahrenheit - 32) * 5/9 
# print(celsius)

# 31 Write a program to find the total and average of N numbers entered by the user.

# N = int(input("Enter the number of values (N): "))
# total = 0
# for i in range(N):
#     num = float(input(f"Enter number {i+1}: "))
#     total += num
# average = total / N if N != 0 else 
# print(f"\nTotal = {total}")
# print(f"Average = {average}")

# 32 Write a program to compute the total bill for buying multiple items (quantity × price).

# items = [(2, 10.50),(1, 5.25),(3, 3.00)]

# total = 0
# for quantity, price in items:
#     total += quantity * price
# print("Total bill amount: ",total)

# 33 Write a program to find the power of a number without using ** (using repeated multiplication).

# number = int(input("Enter the number: "))
# power_raise_to = int(input("Enter the power to raise to: "))

# x = 1
# for _ in range(power_raise_to):
#     x = x * number

# print(f"{number} raised to the power {power_raise_to} is: {x}")

# 34 Write a program to calculate the time taken to cover a distance given speed and distance.

# distance = float(input(" enter the distance in km : "))
# speed = float(input(" enter the speed in km/hr : "))
# time = distance / speed
# print("time taken in hr : ", time)

# 35  Write a program to calculate the total cost of items after GST (Goods and Services Tax).

# price = float(input("enter the full price : "))
# gst_of_product = (price / 100) * 18
# after_gst_price = (price - gst_of_product )
# print("price after gst : ", after_gst_price)

# 36 Write a program to find the number of digits in an integer using arithmetic operators only.

# num = int(input("enter the number to check the number of integers in it : "))

# n = abs(num)
# if n == 0:
#     count = 1
# else:
#     count = 0
#     while n > 0:
#         n = n // 10  
#         count += 1

# print("Number of digits:", count)

# 37 Write a program to reverse a three-digit number using arithmetic operators.

# num = int(input("Enter a three-digit number: "))
# hundreds = num // 100
# tens = (num // 10) % 10
# units = num % 10
# reversed_num = (units * 100) + (tens * 10) + hundreds
# print("Reversed number:", reversed_num)

# 38 Write a program to check if a number is an Armstrong number (use arithmetic operators only).

# 39 Write a program to extract and sum all digits of a 4-digit number.

# 40 Write a program to convert total days into years, weeks, and days using // and %.

# days = int(input("Enter the total number of days : "))
# year = (days // 365)
# month = (days // 29) or (days // 30) or (days // 31)
# week = (days // 7)

# print(f" {days} is {year} year , {month} month , {week} week ")

# 41 Write a program to compute the total fuel cost given distance and mileage.

# distance = int(input("Enter the distance (km): "))
# fuel = int(input("Enter the fuel needed (litres): "))
# mileage = distance / fuel
# print (f"{distance} distance covered in {fuel} litres fuel and mileage got is {mileage} ")

# 42 Write a program to calculate the roots of a quadratic equation using the formula (-b ± sqrt(b**2 - 4ac)) / (2a).

# a = float(input("Enter the value for a: "))
# b = float(input("Enter the value for b: "))
# c = float(input("Enter the value for c: "))

# discriminant = b**2 - 4 * a * c

# if discriminant >= 0:
#     root1 = (-b + discriminant**0.5) / (2 * a)
#     root2 = (-b - discriminant**0.5) / (2 * a)
#     print(f"The roots are {root1} and {root2}")
# else:
#     print("The equation has complex roots (cannot compute without math library)")

# 43 Write a program to compute the distance between two points (x1, y1) and (x2, y2) using the distance formula.

# x1 = int(input( "enter the coordinates of point x1 : " ))
# y1= int(input( "enter the coordinates of point y1 : " ))
# x2= int(input( "enter the coordinates of point x2 : " ))
# y2 = int(input( "enter the coordinates of point y2 : " ))

# distance = ( (x2 - x1) ** 2 - (y2 - y1)**2 ) ** (0.5)
# print(f"distance of ({x1},{y1}) and ({x2},{y2}) is {distance} ")

# 44 Write a program to calculate the slope of a line passing through two given points

# x1 = int(input( "enter the coordinates of point x1 : " ))
# y1= int(input( "enter the coordinates of point y1 : " ))
# x2= int(input( "enter the coordinates of point x2 : " ))
# y2 = int(input( "enter the coordinates of point y2 : " ))

# slope = (y2 - y1) / (x2 - x1)
# print(f"slope of ({x1},{y1}) and ({x2},{y2}) is {slope} ")

# 45 Write a program to find the profit or loss percentage on selling an item.

# original_price = int(input( "enter the original price : " ))
# selling_price = int(input("enter the selling price  : "))
# difference = abs((original_price - selling_price) / original_price) * 100

# if original_price < selling_price :
#     print(f" profit is {difference}% ") 
# elif original_price > selling_price :
#     print (f" loss is {difference}% ")
# else :
#     print (" no profit no loss ")

# 46 Write a program to compute the EMI (Equated Monthly Installment) using the standard formula.

# p = float(input( "enter the principal loan amount you borrowed : " ))
# r = float(input( "enter the monthly interest rate : " ))
# n = float(input( "enter the number of months in your loan tenure : " ))
# emi = (p*r*(1+r)**n) / ((1+r)**n - 1)

# print(f"EMI is {emi}")

# 47 Write a program to compute the perimeter and area of a rectangle using only arithmetic operators and formatted output.

# length = int(input("enter the lenght : "))
# breath = int(input("enter the breath : "))

# perimeter = 2 * (length + breath)
# print(f"perimeter of rectange is {perimeter}")

# 48 Write a program to find the geometric mean and harmonic mean of two numbers.

# first_number = int(input("enter the first number : "))
# second_number = int(input("enter the seconf number : "))
# geometric_mean  = (first_number * second_number) ** 0.5
# harmonic_mean =  (2 * first_number * second_number) / (first_number + second_number)

# print(f"geometric means is {geometric_mean}")
# print(f"harmonic means is {harmonic_mean}")

# 49 Write a program to compute the sum of the first N natural numbers using arithmetic operators only (no loops).

# n = int(input("sum of the first N natural numbers : "))
# formula = (n *( n + 1 ) ) / 2

# print(f"sum of the {n} natural numbers is {formula}")

# 50 Write a program to compute the sum of squares of first N even numbers using arithmetic formula.

# n = int(input("Sum of squares of first N even numbers : "))
# formula = (2*n *(n+1) * (2*n +1)) / 6
# print(f"sum of the {n} natural numbers is {formula}")

# 51 Write a program to convert total seconds into hours, minutes, and seconds using // and %.

# s = int(input("Enter the seconds to convert : "))
# min = (s // 60)
# hr = ((s / 60)/ 60)
# print(f" seconds converted in {min} min and {hr} hr ")

# 52 Write a program to calculate the factorial of a number using only arithmetic operators and loops.

# n = int(input("enter the number : "))
# factorial = 1
# i = 1
# while i <= n:
#         factorial = factorial * i
#         i = i + 1
# print(f"Factorial of {n} is: {factorial}")

# 53 Write a program to compute the volume and surface area of a cylinder.

# r = float(input("radius : "))
# h = float(input("height : "))
# volume = ( 3.14 * r * h ** 2)
# surface_area = (2 * 3.14 * r *(r + h))
# print(f" volume : {volume} and surface area : {surface_area}")

# 54 Write a program to compute the area and perimeter of a square when side length is given.

# side = float(input("side : "))
# area = side ** 2
# perimeter = 4 * side
# print (f"area is {area} and perimter is {perimeter}")

# 55 Write a program to find the simple and compound interest for multiple years and compare them.

# p = float(input( "enter the principal amount : " ))
# r = float(input( "enter the interest rate : " ))
# t = float(input( "enter the time (year) : " ))

# simple_interest = (p*r*t)/100
# compound_interest = ((p)* (1 + (r/100))**t ) - p

# print(f"simple interest is {simple_interest} and compound interest is {compound_interest}")

# 56 Write a program to calculate the depreciation value of an asset using the straight-line method.

# cost = int(input("Enter price: "))
# salvage_value = int(input("Enter salvage value: "))
# useful_life = int(input("Enter the used life in years: "))    
# depreciation = (cost - salvage_value) / useful_life
# print("Annual depreciation is:", depreciation)

# 57 Write a program to compute the distance covered under uniform acceleration using formula s = ut + 1/2 * a * t**2.

# t = int(input("Enter the time (seconds) : "))
# u = int(input("Enter the initial velocity (meters/seconds) : "))
# a = int(input("Enter the acceleration (meter/seconds square) :  "))
# s = u*t + (1/2 * a * t**2)
# print(f"displacement is {s}")

# 58 Write a program to calculate speed given distance and time (from multiple trips).

# def speed(distance, time):
#     return distance/time

# n = int(inpt("Enter the number of trips : "))
# def speed(distance, time):
#     return distance / time

# n = int(input("Enter the number of trips: "))

# for i in range(1, n + 1):
#     distance = float(input(f"Enter distance for trip {i} (in meters): "))
#     time = float(input(f"Enter time for trip {i} (in seconds): "))
#     s = speed(distance, time)
#     print(f"Speed for trip {i} is {s} m/s\n")


# 59 Write a program to simulate a shopping cart total with discount and GST calculation.


# 60 Write a program to calculate final exam marks using weighted average of assignments, midterm, and final exam.

# 61 Write a program that accepts three sides of a triangle and determines if it is equilateral, isosceles, or scalene using arithmetic relations.

# a = int(input("first side : "))
# b = int(input("second side : "))
# c = int(input("third side : "))

# if int(a == b) and int(a == c) and (b == c):
#     print("It is a equilateral triangle")

# elif int(a != b) and int(b != c) and int(a !=c):
#     print("It is a scalene triangle")
# else :
#     print("It is a isocelese triangle ")