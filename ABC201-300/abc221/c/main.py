N = input()
n = len(N)

ans = 0
# ０から(1<<n)-1まで全探索。
for i in range(1 << n):
    num1 = []
    num2 = []
    for j in range(n):
        wari = 1 << j
        if (i // wari) % 2 == 1:
            num1.append(N[j])
        else:
            num2.append(N[j])
    if len(num1) == 0 or len(num2) == 0:
        continue
    num1.sort(reverse=True)
    num2.sort(reverse=True)
    number_1 = int("".join(num1))
    number_2 = int("".join(num2))
    product = number_1 * number_2
    ans = max(ans, product)
print(ans)
