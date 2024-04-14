from collections import defaultdict

q = int(input())
prime_number = defaultdict(int)
number_2017 = defaultdict(int)
prime_number[2] = 1
for i in range(3, 10**5 + 1, 2):
    is_prime = True
    for j in range(2, i):
        if j**2 > i:
            break
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_number[i] = 1
        if prime_number[(i + 1) // 2] == 1:
            number_2017[i] = 1
ans = [0]
for i in range(1, 10**5 + 1):
    if i % 2 == 0:
        ans.append(ans[i - 1])
        continue
    if number_2017[i] == 1:
        ans.append(ans[i - 1] + 1)
    else:
        ans.append(ans[i - 1])
for i in range(q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])
