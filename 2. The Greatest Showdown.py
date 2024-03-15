# Objective:
# Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

x, y, z = input("Input three different numbers in the format: x y z \n").split()
print("Your numbers are:",x, y, z)

if x > y and x > z:
    print("The greatest number is:",x)
elif y > x and y > z:
    print("The greatest number is:", y)
else:
    print("The greatest number is:",z)

# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest 
# number among the three and print it out.
    
x, y, z = input("Input three different numbers in the format: x y z \n").split()
print("Your numbers are:",x, y, z)

if x > y and x > z:
    print("The greatest number is:",x)
elif y > x and y > z:
    print("The greatest number is:", y)
else:
    print("The greatest number is:",z)

if x < y and x < z:
    print("The smallest number is:",x)
elif y < x and y < z:
    print("The smallest number is:", y)
else:
    print("The smallest number is:",z)

# Task 3: Equality Check
# Enhance your program to handle cases where two or 
# all of the numbers are equal. The program should 
# display appropriate messages like 
# "Two numbers are equal and the largest" or "All numbers are equal".
    
x, y, z = input("Input three numbers in the format: x y z \n").split()
print("Your numbers are:",x, y, z)

if x > y and x > z:
    print("The greatest number is:",x)
elif y > x and y > z:
    print("The greatest number is:", y)
elif x == y and x > z:
    print(x,"and",y,"are equal and greater than",z)
elif x == y and x < z:
    print(x,"and",y,"are equal and less than",z)
elif x == z and z < y:
    print(x,"and",z,"are equal and less than",y)
elif x == z and z > y:
    print(x,"and",z,"are equal and greater than",y)
elif z == y and z > x:
    print(y,"and",z,"are equal and greater than",x)
elif z == y and z < x:
    print(y,"and",z,"are equal and less than",x)
elif z == y and z == x:
    print(y,",",z,"and",x,"are all equal")
else:
    print("The greatest number is:",z)

if x < y and y < z:
    print("The smallest number is:",x)
elif y < x and x < z:
    print("The smallest number is:", y)    
elif x == y and x > z:
    print(x,"and",y,"are equal and greater than",z)
elif x == y and x < z:
    print(x,"and",y,"are equal and less than",z)
elif x == z and z < y:
    print(x,"and",z,"are equal and less than",y)
elif x == z and z > y:
    print(x,"and",z,"are equal and greater than",y)
elif z == y and z > x:
    print(y,"and",z,"are equal and greater than",x)
elif z == y and z < x:
    print(y,"and",z,"are equal and less than",x)
elif z == y and z == x:
    print(y,",",z,"and",x,"are all equal")
else:
    print("The smallest number is:",z)