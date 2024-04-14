from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
different = list()
for i in range(n // 2):
    if a[i] != a[n - 1 - i]:
        different.append([min(a[i], a[n - 1 - i]), max(a[i], a[n - 1 - i])])
num = defaultdict(int)
ans = 0
# numでどの数字がどの数字に置き換わっているか管理。
# 最初は、ある数字を自身の数字で初期化。
for i in different:
    num[i[0]] = i[0]
    num[i[1]] = i[1]
ans = 0
different.sort(reverse=True)
while len(different) > 0:
    dif = different.pop()
    if num[dif[0]] != num[dif[1]]:
        ans += 1
        if num[dif[0]] < num[dif[1]]:
            num[dif[1]] = num[dif[0]]
        else:
            num[dif[0]] = num[dif[1]]
print(ans)
