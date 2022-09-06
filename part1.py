#!/usr/bin/python3
# coding=utf-8


# Calculate simple interest by gathering three things (principle, number of years, rate of interest).


# Get user input for p (p = principle).

p = input(" Please enter an amount for principle. ")
# Get user input for n (n = number of years).
n = input(" Please enter an amount for years. ")
# Get user input for r (r = rate of interest).
r = input(" Please enter an amount for interest. ")
# Convert user inputs p, n, r to int(). (Links to an external site.)
p = int(p)
n = int(n)
r = int(r)

# Calculate the simple interest of p, n, r (multiple p, n, r, and then divide by 100).
SimpleInterest = (p*n*r)/100
# Print out the simple interest value.
print(SimpleInterest)

