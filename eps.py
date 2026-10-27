number = int(input('Enter a number '))
x = 0
epsilon = 0.01
num_guess = 0
increment = 0.00001
while abs((x**2-number)) > epsilon and x**2 <= number:
          x = x + increment
          num_guess += 1
          if num_guess%1000 == 0:
                            print('Current_guess', x)
print(x , num_guess)