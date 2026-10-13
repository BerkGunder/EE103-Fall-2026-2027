given_number=int(input('Enter a number: '))
a = 0
if given_number < 0:
    print('You have made a mistake ')
else:
    given_number = given_number ** 0.5
    while True:
        a = a + 1
        if given_number == a:
            print(given_number)
            break
        elif given_number < a:
            print('The given number is not a perfect square')
            break


