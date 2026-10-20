s = 'abca'
x = 0
seen = ''
for i in range(len(s)):
    if s[i] not in seen:
        seen = seen + s[i]
        x += 1
print(x)

