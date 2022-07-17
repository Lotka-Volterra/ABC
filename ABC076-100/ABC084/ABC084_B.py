a, b = map(int, input().split())
s = input()
num = '0123456789'
ans = 'Yes'
for i in range(a+b+1):
    if i == a:
        if s[i] != '-':
            ans = 'No'
    else:
        if s[i] not in num:
            ans = 'No'
print(ans)

#0-9の数字が含まれるかの判断は、'0'<=s[i]<='9'でもできる
