# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

def sum_of_digits():
    # Ask the user for a 4-digit integer
    number = input("Please enter a 4-digit integer: ")

    # Check if the input is exactly 4 digits and numeric
    if len(number) == 4 and number.isdigit():
        # Convert each character to an integer and sum them up
        digits = [int(digit) for digit in number]
        total_sum = sum(digits)
        
        # Create the output string for the result
        result_str = " + ".join(number) + " = " + str(total_sum)
        
        # Print the formatted result
        print(result_str)
    else:
        print("The input is not a valid 4-digit number. Please try again.")

# Call the function
sum_of_digits()