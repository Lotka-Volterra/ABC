s, t, x = map(int, input().split())
if s <= x < t:
    print('Yes')
elif t < s:
    if s <= x or x < t:
        print('Yes')
    else:
        print('No')
else:
    print('No')
