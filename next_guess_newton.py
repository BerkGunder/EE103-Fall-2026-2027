x = int(input('What x to find the square root of? '))
g = int(input('What guess to start with? '))
print(g)
f = g**2 - x
fd = g*2
ng = g - f/fd
print(ng)