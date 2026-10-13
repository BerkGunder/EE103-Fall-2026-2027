n = int(input('Enter a number: '))
a = 0
for i in range (1, n+1):
    a = a + i
sum_gauss = (n * (n + 1)) / 2
if a == sum_gauss:
    print('My running sum code works correctly')
else:
    print('My running sum code failed badly')