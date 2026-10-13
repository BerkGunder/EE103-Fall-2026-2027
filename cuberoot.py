x = int(input('Enter a number: '))
if x < 0:
    print(-(-x) ** (1/3))
else:
    print(x ** (1/3))
