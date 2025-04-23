"""
compound.py
This program calculate the compound intrest

Expression:

To calculate compound interest, use the formula total = P * (1 + (r/n))^(nt)

P = principle
R = annual interest rate / 100
N = compounding frequency per year
T = time in yearss
"""

P = int(input("Enter the principle amount: "))
R = int(input("Enter the intrest of rate: "))
N = int(input("Enter the number of times: "))
T = int(input("Enter the time in years: "))

total = P * ((1 + ((R/100)/N)) ** (N*T))
print("Total amount after", T, "years: ", total)

# Compound Interest earned:
CI = total - P 
print("Compound interest earned: ", CI)
