x = input('Enter a number ')
x = float(x)
p = 0 
a = int(x)
b = x - int(x)
c = ''
g = ''
precision = 10
result = ''
if x == 0:
    result = '0'
while a > 0:
    c = str(a%2)
    a = a // 2
while b > 0 and len(g) < precision:
    d = (b*(2**p))
    f = int(d)
    g = str(f) + g
    p = p + 1
result = c + '.' + g[::-1]
print(result)


