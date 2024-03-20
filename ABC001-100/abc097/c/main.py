s = list(input())
k = int(input())
words = set()
len_s = len(s)
for i in range(1, 6):
    for j in range(len_s + 1 - i):
        words.add("".join(s[j : j + i]))
words = sorted(list(words))
print(words[k - 1])
