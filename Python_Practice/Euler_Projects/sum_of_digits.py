total_sum = 0
number = int(input("Enter a number: "))

while number > 0:
    total_sum += number % 10
    number //= 10
    if number == 0 and total_sum > 10:
        number = total_sum
        total_sum = 0
print(total_sum)    
