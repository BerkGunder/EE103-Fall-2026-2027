from secret_number import secretNum
a = int(input('Enter a number '))
x = 0
b = 0
while a != secretNum and x < 5:
    x = x +1
    if a < secretNum:
        print('Your number is lower than the secret number')
    elif a > secretNum:
        print('Your number is higher than the secret number')
    a = int(input('Enter a number '))
if x > 4:
    while True:
        print('Oh no!')
else:
    print('You guessed it right!')
