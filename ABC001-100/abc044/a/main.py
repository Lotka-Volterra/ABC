n = int(input())
k = int(input())
x = int(input())
y = int(input())
shukuhakuhi = 0

for i in range(1, n+1):
    if i > k:
        shukuhakuhi += y
    else:
        shukuhakuhi += x
print(shukuhakuhi)

# 別解
# k日まで
hiyou_until_k = x*min(n, k)
# k+1日後
hiyou_after_k = y*max(0, n-k)
print(hiyou_until_k+hiyou_after_k)

# 公式解答例
if n <= k:
    print(n*x)
else:
    print(k*x+(n-k)*y)
