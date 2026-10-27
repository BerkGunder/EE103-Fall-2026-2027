number = int(input('Enter a number '))
result = ''
if number == 0:
    result = '0'
while number > 0:
    result = str(number%2) + result
    number = number // 2
print(result)