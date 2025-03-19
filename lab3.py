#  program 1

# Find Numbers Divisible by 7 and 5 Between 1500 and 2700

# Create an empty list to store the numbers
divisible_numbers = []

# Use a loop to check each number from 1500 to 2700
for num in range(1500, 2701):
    #  Check if the number is divisible by both 7 and 5
    if num % 7 == 0 and num % 5 == 0:
        #  If the condition is met, add the number to the list
        divisible_numbers.append(num)

#  Print the final list of numbers
print(divisible_numbers)






#program 2



# Convert Temperature Between Celsius and Fahrenheit



#  Ask the user to enter a temperature value
temperature = float(input("Enter temperature value: "))

#  Ask the user to specify the conversion type
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

# Convert based on the chosen unit
if unit == "C":
    fahrenheit = (9/5) * temperature + 32
    print(f"{temperature}°C is {fahrenheit}°F")
elif unit == "F":
    celsius = (5/9) * (temperature - 32)
    print(f"{temperature}°F is {celsius}°C")
else:
    print("Invalid unit! Please enter C or F.")






#program 3



#Guess the Number Between 1 and 9

import random

# Generate a random number between 1 and 9
secret_number = random.randint(1, 9)

#  Start a loop to take user guesses
while True:
    guess = int(input("Guess a number between 1 and 9: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Well guessed!")
        break  # Exit the loop if the guess is correct
    else:
        print("Try again!")  # Ask the user to guess again



#program 4


# Print a Star Pattern

#  Print the first half of the pattern
for i in range(1, 6):  # Loop from 1 to 5
    print("" * i)

# Print the second half of the pattern
for i in range(4, 0, -1):  # Loop from 4 to 1 (decreasing)
    print("" * i) 



# program 5



# Reverse a Word

#  Take user input
word = input("Enter a word: ")

# Reverse the word
reversed_word = word[::-1]

# Print the reversed word
print("Reversed word:", reversed_word)



#program 6


#Count Even and Odd Numbers

#  Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

#  Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        even_count += 1  # Increase even counter
    else:
        odd_count += 1  # Increase odd counter

# Print the counts
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")



#program 7


# Print Data Types of List Elements

# Define a list with different data types
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

#  Loop through each item in the list
for item in datalist:
    print(f"Item: {item}, Type: {type(item)}")  



# program 8



# Print Numbers from 0 to 6 Except 3 and 6

# Loop from 0 to 6
for num in range(7):
    # Skip numbers 3 and 6
    if num == 3 or num == 6:
        continue
    print(num, end=" ") 






#program 9

# Fibonacci Series from 0 to 50



#The Fibonacci series starts with 0 and 1. Each next number is the sum of the previous two numbers.

#  Initialize the first two Fibonacci numbers
a, b = 0, 1

#  Print the first number
print(a, end=" ")

# Generate Fibonacci numbers until 50
while b <= 50:
    print(b, end=" ")
    a, b = b, a + b  


# program program after 9


# FizzBuzz for Numbers 1 to 50

"""

If a number is divisible by 3, print "Fizz".

If a number is divisible by 5, print "Buzz".

If a number is divisible by both 3 and 5, print "FizzBuzz".  """


#  Loop from 1 to 50
for num in range(1, 51):
    #  Check divisible conditions
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)  # Print the number if not divisible by 3 or 5


#program 10



# Generate a 2D Array Using Multiplication


#  Take input for rows and columns
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

#  Create an empty 2D list
array = []

#  Generate values for each row
for i in range(m):
    row = []  # Create an empty row
    for j in range(n):
        row.append(i * j)  # Multiply row index with column index
    array.append(row)  # Add row to the array


print(array)





# program 11


#Convert Text to Lowercase (Multiple Lines)



# Create an empty list to store lines
lines = []

#  Read lines from the user
while True:
    line = input("Enter a line (press Enter to stop): ")
    if line == "":  # Stop when user enters a blank line
        break
    lines.append(line.lower())  # Convert to lowercase and store

for line in lines:
    print(line)



# program 12

# Find Binary Numbers Divisible by 5


#  Take input from the user
binary_numbers = input("Enter comma-separated binary numbers: ").split(",")

# Check divisibility by 5
divisible_by_5 = []
for binary in binary_numbers:
    decimal = int(binary, 2)  # Convert binary to decimal
    if decimal % 5 == 0:
        divisible_by_5.append(binary)


print(",".join(divisible_by_5))






#program 13
# Count Letters and Digits in a String

#  Take user input
text = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

#Loop through each character in the string
for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

# Step 4: Print the results
print("Letters:", letters)
print("Digits")



# program 14
# Password Validation

"""

Password Rules:

1. At least one uppercase letter (A-Z).


2. At least one lowercase letter (a-z).


3. At least one digit (0-9).


4. At least one special character ($#@).


5. Length must be between 6 and 16 characters.
                                                               """


import re

# Take user input
password = input("Enter password: ")

# Define password rules using regex
if (6 <= len(password) <= 16 and
    re.search("[a-z]", password) and
    re.search("[A-Z]", password) and
    re.search("[0-9]", password) and
    re.search("[$#@]", password)):
    print("Valid Password")
else:
    print("Invalid Password")













