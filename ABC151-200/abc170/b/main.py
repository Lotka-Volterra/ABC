x, y = map(int, input().split())
for i in range(x+1):
    if y == i*2+(x-i)*4:
        print('Yes')
        quit()
print('No')

# 別解　答えがYesである必要十分条件は、2*x<=y<=4*x
x, y = map(int, input().split())
if 2*x <= y <= 4*x:
    print('Yes')
else:
    print('No')
