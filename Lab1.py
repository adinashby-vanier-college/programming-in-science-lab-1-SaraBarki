# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    pass  # Replace with your code

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function
    pass  # Replace with your code


#Simple Hello World Program

print('Hello, World!')

#Write a Python program that asks the user to input their name (string), age (integer), and height (float), and then displays them back to the user with an appropriate message.

#Get the individual's name, age and height.

name = str(input('Enter your name '))
age = int(input('Enter your age '))
height = float(input('Enter your height '))

#Greet the individual and display their name, age and height

print(f'Hello,{name}')
print(f'You are {age} years old')
print(f'Your age {height} meters')