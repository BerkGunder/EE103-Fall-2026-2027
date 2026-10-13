x = int(input('What number to find the cube root of? '))
g = int(input('What guess to start with? '))
f = g**3 -x
print(f)
ng = (g) - (g**3-x)/(3*g**2)
print(ng)
