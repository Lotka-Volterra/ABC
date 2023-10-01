n = int(input())
s = input()
acc = "b"
if acc == s:
    print(0)
    quit()
for i in range(1, 50):
    if i % 3 == 0:
        acc = "b" + acc + "b"
    elif i % 3 == 1:
        acc = "a" + acc + "c"
    else:
        acc = "c" + acc + "a"
    if s == acc:
        print(i)
        quit()
print(-1)
