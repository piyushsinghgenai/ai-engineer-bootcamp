radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of Circle =", area)


celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After Swapping")
print("a =", a)
print("b =", b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)


principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)



name = input("Enter Student Name: ")

marks1 = float(input("Enter Marks for Subject 1: "))
marks2 = float(input("Enter Marks for Subject 2: "))
marks3 = float(input("Enter Marks for Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n----- RESULT -----")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", percentage)