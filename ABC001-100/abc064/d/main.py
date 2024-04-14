n = int(input())
s = input()
stack = []
for i in range(n):
    if len(stack) > 0:
        last = stack.pop()
        if not (last == "(" and s[i] == ")"):
            stack.append(last)
            stack.append(s[i])
    else:
        stack.append(s[i])
# print(stack)
left_count = 0
right_count = 0
for i in stack:
    if i == ")":
        left_count += 1
    else:
        right_count += 1
print("(" * left_count + s + ")" * right_count)
