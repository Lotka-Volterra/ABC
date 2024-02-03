from curses.ascii import isupper


s = input()
n = len(s)
Ccount = 0
for i in range(n):
    if i == 0:
        if s[i] != 'A':
            print('WA')
            quit()
    elif 2 <= i <= n-2:
        if s[i] == 'C':
            Ccount += 1
            if Ccount > 1:
                print('WA')
                quit()
    else:
        if s[i].isupper():
            print('WA')
            quit()
if Ccount == 0:
    print('WA')
else:
    print('AC')

# 公式解答
s = input()
n = len(s)
ans = 'AC'
if s[0] != 'A':
    ans = 'WA'
count = 0
for i in range(1, n):
    if s[i].isupper():
        # 最初から3つ目から末尾から2つ目の間以外に大文字がある場合、
        # および最初から3つ目から末尾から2つ目の区間にC以外の大文字がある場合
        if i == 1 or i == n-1 or s[i] != 'C':
            ans = 'WA'
        else:
            count += 1
if count != 1:
    ans = 'WA'
print(ans)
