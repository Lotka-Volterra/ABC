a, b = map(int, input().split())
if a > 0 and b == 0:
    print('Gold')
elif a == 0 and b > 0:
    print('Silver')
else:
    print('Alloy')
# 簡潔に
a, b = map(int, input().split())
if b == 0:
    print('Gold')
elif a == 0:
    print('Silver')
else:
    print('Alloy')
