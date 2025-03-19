# lab 2


# while loop implementation




count = 0

while (count <3):
    count = count + 1

    print("Hello Geek")



#single staement while loop



count=0

while (count==0): print("hello geek")





# implementation of for loop





# Iterating Over a List

#program 1

print("List Iteration") 

# Defining a list with three elements
l = ["geeks", "for", "geeks"]

# Looping through each element in the list
for i in l:
    print(i)  # Printing each element of the list



# Program 2:
# Iterating Over a Tuple



print("\nTuple Iteration") 

# Defining a tuple with three elements
t = ("geeks", "for", "geeks")


for i in t:
    print(i)  # Printing each element of the tuple



#Program 3: 
#Iterating Over a String



print("\nString Iteration") 

# Defining a string
s = "Geeks"

for i in s:
    print(i)  # Printing each character of the string


#Program 4: 
#Iterating by Index of Sequence


print("\nIterating by Index")

# Defining a list with three elements
list_ = ["geeks", "for", "geeks"]

# Using index to iterate through the list
for index in range(len(list_)):  
    print(list_[index])  # Printing each element using index



#  Implementation of continue statement 


# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
           continue
    print ('Current Letter:'), letter
     







#  Implementation of break statement 



for letter in 'geeksforgeeks':
    if letter == 'e' or letter =='s':
        break
    print('Current Letter:'), letter





# implementation of functions




# Program 1: Function with Parameter

# Function that takes a parameter 
def my_function(fname):
    print(fname + " Refsnes")

# Calling the function with different arguments
my_function("Emil")
my_function("Tobias")
my_function("Linus")




# Program 2: Function with Default Parameter Value

# Function with a default parameter value
def my_function(country="Norway"):
    print("I am from " + country)

# Calling the function with different arguments
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




# Program 3: Passing a List as a Parameter

# Function that takes a list as a parameter
def my_function(food):
    for x in food:
        print(x)

# Defining a list and passing it to the function
fruits = ["apple", "banana", "cherry"]
my_function(fruits)




# implementation of class bject,__init function ,function in class concepts






# Defining a class named Person
class Person:
    # Constructor to initialize name and age attributes
    def _init_(self, name, age):
        self.name = name
        self.age = age

    # Method to print a greeting message
    def myfunc(self):
        print("Hello my name is " + self.name)

# Creating an object of the Person class
p1 = Person("John", 36)
p1.myfunc()  # Calling the method on the object



#                                                  lab 2 end















