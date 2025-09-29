#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:  # keeps the whole program looping
    user_input = input("Enter the amount of terms of the Fibonacci sequence you want?")
    # first get the user to input how many sequences they want useing the input function

    while user_input.isdigit() == False or int(user_input) <= 0:
    #  if the user input whuch is supposed to be a digit is false
    #( so not a digit) or the int is less than or equal to zero
        print("Please enter a postive integer.") # tell them to print positive val
        user_input = input("enter the amount of terms of the Fibonacci sequence you want?")
    # goes back to wanting input using input function
    user_input = int(user_input) # the input function is a string convert to int

    a, b = 0, 1 # fisrt two numbers in the fibbonaci seq
    for i in range(user_input):# for loop
        print(a)
        next_term = a + b
        a = b 
        b = next_term        
