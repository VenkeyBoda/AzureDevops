# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

number = int(input("Enter a number: "))
index = 1
result = 0
while index < number:
    is_multiple = (index % 3 == 0) or (index % 5 == 0)
    if is_multiple == True:
        result = result +  index
    index = index + 1
print(result)       
