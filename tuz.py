for a in range (11):
    for b in range (11):
        for c in range(11):
            total = (a + b + c == 10)
            two_less = (b == a - 2)
            twice = (c == a*2)
            if total and two_less and twice:
                print(f'alyssa {a}')
                print(f'ben {b}')
                print(f'cindy{c}')