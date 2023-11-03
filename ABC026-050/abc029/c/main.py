n = int(input())
words = []


def word(s):
    if len(s) == n:
        words.append(s)
    else:
        for i in range(3):
            word(s + "abc"[i])


word("")
words.sort()
for i in range(len(words)):
    print(words[i])
