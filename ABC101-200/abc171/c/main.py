n = int(input()) - 1
ans = chr(n % 26 + ord("a"))
n //= 26

while n > 0:
    n -= 1
    ans = chr(n % 26 + ord("a")) + ans
    n //= 26
print(ans)
