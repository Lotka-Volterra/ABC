f = [0] * 11
f[0] = 1
n = int(input())
for i in range(1, n + 1):
    f[i] = i * f[i - 1]
print(f[n])

# f(n)=n!である、つまり階乗であるため
import math

print(math.factorial(int(input())))


# 再帰関数
def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)


print(f(int(input())))
