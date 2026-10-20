s = 'abcabc'
seen = ''
for index in range(len(s)):
    if s[index] not in seen:
        seen = seen + s[index]
print(seen)
