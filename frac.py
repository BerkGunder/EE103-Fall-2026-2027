x = float(input('Enter a number '))
a = int(x)
b = x - a
result = ''
if a == 0:
    result = '0'
while a > 0:
    c = str(a%2) + c
    a = a // 2
print(c)
