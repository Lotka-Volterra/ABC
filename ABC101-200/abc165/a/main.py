k = int(input())
a, b = map(int, input().split())
ans = "NG"
for i in range(a, b+1):
    if i % k == 0:
        ans = "OK"
print(ans)

# 公式別解　b以下のkの倍数の最大値を求め、それがa以上か調べる
k = int(input())
a, b = map(int, input().split())
largest = (b//k)*k
if largest >= a:
    print("OK")
else:
    print("NG")

# 変形すると
if b//k > (a-1)//k:
    print("OK")
else:
    print("NG")
