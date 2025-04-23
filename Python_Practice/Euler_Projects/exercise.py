a = 1
b = 2
c = 0
sum = 2
c = a + b
while a + b < 100:
    c = a + b
    print(c)
    if c % 2 == 0:
        sum = sum + c
    a = b
    b = c
print(sum)

