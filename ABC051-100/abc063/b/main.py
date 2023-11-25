s = input()
alph = [0] * 26
for i in s:
    alph[ord(i) - ord("a")] += 1
for i in range(26):
    if alph[i] > 1:
        print("no")
        quit()
print("yes")
