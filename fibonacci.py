#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

user_input = input("Enter how many terms of the Fibonacci sequence you want: ")

print(f'User input: "{user_input}"')

#Validate input
if user_input.isdigit() and int(user_input) > 0:
    n = int(user_input)

    #Generate sequence
    a = 0
    b = 1
    output = []
    for i in range(n):
        output.append(str(a))
        a, b = b, a + b

    #Print result
    print("Expected output:", " ".join(output))
else:
    print('Expected output: "Please enter a positive integer."')
    
