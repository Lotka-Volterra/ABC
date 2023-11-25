x, y = map(int, input().split('.'))
a = ''
if 0 <= y <= 2:
    a = '-'
elif 7 <= y <= 9:
    a = '+'
print(str(x)+a)
