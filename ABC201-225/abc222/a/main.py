n = input()
while len(n) < 4:
    n = '0' + n
print(n)

#公式解答
N=int(input())
print(f"{N:04d}")