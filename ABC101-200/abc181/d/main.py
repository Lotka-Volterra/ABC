s = input()
s_dict = [0] * 10
for i in s:
    s_dict[int(i)] += 1
for i in range(10 ** (min(3, len(s)) - 1) + 1, 10 ** (min(3, len(s))) + 1):
    if i % 8 != 0:
        continue
    num_dict = [0] * 10
    for j in str(i):
        num_dict[int(j)] += 1
    ok = True
    for j in range(10):
        if s_dict[j] < num_dict[j]:
            ok = False
            break
    if ok:
        print("Yes")
        quit()
print("No")
