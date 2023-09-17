a, b, c, d = map(int, input().split())
if b <= min(a, c) or max(a, c) <= b:
    if abs(a-c) <= d:
        print('Yes')
    else:
        print('No')
else:
    if abs(a-b) <= d and abs(c-b) <= d:
        print('Yes')
    else:
        print('No')
# もっとスマートに
a, b, c, d = map(int, input().split())
ab = abs(a-b)
bc = abs(c-b)
ac = abs(a-c)
if ac <= d:
    print('Yes')
elif ab <= d and bc <= d:
    print('Yes')
else:
    print('No')
