secret_num = int(input('Enter a number '))
found = False
for i in range(1,11):
    if i == secret_num:
        print(i)
        found = True
if not found:
    print('lol')
    