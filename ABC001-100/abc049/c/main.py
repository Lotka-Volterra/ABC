s = input()
len_s = len(s)
s = "".join(list(reversed(s)))
ind = 0
ok = True
while True:
    if ind + 4 < len_s and (s[ind : ind + 5] == "esare" or s[ind : ind + 5] == "maerd"):
        ind += 5
    elif ind + 5 < len_s and s[ind : ind + 6] == "resare":
        ind += 6
    elif ind + 6 < len_s and s[ind : ind + 7] == "remaerd":
        ind += 7
    else:
        ok = False
        break
    if ind >= len_s:
        break

print("YES") if ok else print("NO")
