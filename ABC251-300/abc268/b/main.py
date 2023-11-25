s = input()
t = input()
if len(t) >= len(s) and s == t[: len(s)]:
    print("Yes")
else:
    print("No")
