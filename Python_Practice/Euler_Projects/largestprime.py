def is_prime(number):
    result = True
    index = 2
    while index < number:
        if number % index == 0:
            result = False
            break
        index = index + 1
    return result

number = int(input("enter a number: "))
for index in range(2, number):
    if number % index == 0 and is_prime(index):
            print(index)
