n = 0
where = input('Left or right? ')
while where == 'right':
    n = n + 1
    if n > 2:
     print(':(')
    where = input('left or right? ')
print('You escaped ')