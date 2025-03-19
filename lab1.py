#implementaiton  of print function
print("hello world")


# Program with Comments in Python

x = 1
# The initial value of x is 1.
if x > 0:
    print("These are two comments")  


# Input/Output in Python

txt = input("Type something to test this out: ")
print(txt)






#multiple statements on single line
print("statement1");print("statement2")








# Program with Single Space Indentation

x = 1
if x > 0:
 print("This statement has a single space Indentation")
 print("This statement has a single space Indentation")


# Program with Single Tab Indentation

x = 1
if x > 0:
	print("This statement has a single tab Indentation")
	print("This statement has a single tab Indentation")






#Integer and Float Data Types in Python

# Integer values
a = 1452
print(type(a))  # Output: <class 'int'>

b = -4587
print(type(b))  # Output: <class 'int'>

c = 0
print(type(c))  # Output: <class 'int'>

# Float values
g = 9.31
print(type(g))  # Output: <class 'float'>

h = -11.23
print(type(h))  # Output: <class 'float'>

i = .34
print(type(i))  # Output: <class 'float'>

j = 2.2e-10
print(type(j))  # Output: <class 'float'>





# Complex Numbers in Python

# Creating complex numbers
x = complex(1, 2)  # 1 + 2j
print(type(x))  # Output: <class 'complex'>
print(x)  # Output: (1+2j)

# Another way to define a complex number
z = 1 + 2j
print(type(z))  # Output: <class 'complex'>
print(z)  # Output: (1+2j)

# Adding complex numbers
z = z + 1 + 2j
print(type(z))  # Output: <class 'complex'>
print(z)  # Output: (2+4j)






#Boolean (bool) in Python

# Boolean values in Python
x = True
print(type(x))  # Output: <class 'bool'>

y = False
print(type(y))  # Output: <class 'bool'>






#Strings in Python

# Defining strings with single and double quotes
str1 = "String"  # Strings start and end with double quotes
print(str1)  



# Using single quotes inside double quotes
str2 = "Day's"  # Single quote within double quotes
print(str2)  # Output: Day's

# Using double quotes inside single quotes
str3 = 'Day"s'  # Double quote within single quotes
print(str3)  





#Special Characters in Strings 


print("The is a backlash (\\) mark.")  
print("This is tab \t key")  
print("These are \'single quotes\'")  
print("These are \"double quotes\"")  
print("This is a new line\nNew line")







#Python List Indexing Example 

color_list = ["RED", "Blue", "Green", "Black"]  # The list has four elements, indices start at 0 and end at 3

print(color_list[0])  # Return the first element
print(color_list[0], color_list[3])  # Print first and last elements
print(color_list[-1])  # Return last element













#Python List Creation Example


my_list1 = [5, 12, 13, 14]  
print(my_list1)  


my_list2 = ['red', 'blue', 'black', 'white']  
print(my_list2)  


my_list3 = ['red', 12, 112.12]  
print(my_list3)







#Python List Slicing 

color_list = ["RED", "Blue", "Green", "Black"]  # The list has four elements, indices start at 0 and end at 3

print(color_list[0:2])  # Cut first two items
print(color_list[1])    # Cut second item
print(color_list[1:-2]) 
print(color_list[:3])   
print(color_list[:])   








































