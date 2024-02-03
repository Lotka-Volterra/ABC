import math


def mohan(N):
    ans = 0
    for a in range(1, N + 1):
        if a * a * a > N:
            break
        for b in range(a, N + 1):
            if a * b * b > N:
                break
            ans += N // a // b - b + 1
    return ans


def myAns(n):
    ans = 0
    for a in range(1, math.floor(n ** (1 / 3)) + 1):
        for b in range(a, math.floor(n ** (1 / 2)) + 1):
            if n / (a * b) > b:
                ans += (n // (a * b)) - (b - 1)
                print(a, b)
            elif n / (a * b) == b:
                ans += 1
                print(a, b)
            else:
                break
    return ans


# for i in range(64, 126):
#     if mohan(i) != myAns(i):
#         print(mohan(i), myAns(i))
myAns(64)
print(math.floor(64 ** (1 / 3)))
# たとえば64が入力されたとき、WAになる。
# これは、math.floor(64 ** (1 / 3))が浮動小数点演算の関係か3になってしまうため（3.999999999とかのceilで3になっていると考えられる）
