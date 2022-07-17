W = input()
boin = ["a", "i", "u", "e", "o"]
word = ""
for i in W:
    if i in boin:
        continue
    else:
        word += i
print(word)

#別解　母音を置き換える
w = input()
vowels = "aiueo"

for v in vowels:
    w = w.replace(v, "")

print(w)

#書き換えるなら、if i in boinをif i not in boinにして、continueの部分をなくす
W = input()
boin = ["a", "i", "u", "e", "o"]
word = ""
for i in W:
    if i not in boin:
        word += i
print(word)