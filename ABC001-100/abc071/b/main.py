alph = [0] * 26
s = input()
for i in s:
    alph[ord(i) - ord("a")] += 1
for i in range(26):
    if alph[i] == 0:
        print(chr(ord("a") + i))
        quit()
print("None")
