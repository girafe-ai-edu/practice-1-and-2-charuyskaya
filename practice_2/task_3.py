# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = float(input("Please enter your weight "))
height = float(input("Please enter your height in m2 "))

bmi = weight/(height**2)

print(f"Your BMI is : {bmi:.2f}")

