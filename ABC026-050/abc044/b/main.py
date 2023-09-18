w = input()
alp = [0] * 26
for i in range(len(w)):
    alp[ord(w[i]) - ord("a")] += 1
for i in range(26):
    if alp[i] % 2 == 1:
        print("No")
        quit()
print("Yes")
