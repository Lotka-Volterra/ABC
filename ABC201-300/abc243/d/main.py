n, x = map(int, input().split())
s = input()
stack = []
for i in range(n):
    if s[i] == "U" and len(stack) != 0:
        pre = stack.pop()
        if pre == "U":
            stack.append(pre)
            stack.append(s[i])
    else:
        stack.append(s[i])
for i in stack:
    if i == "U":
        if x % 2 == 1:
            x -= 1
        x //= 2
    elif i == "L":
        x *= 2
    else:
        x = x * 2 + 1
print(x)
