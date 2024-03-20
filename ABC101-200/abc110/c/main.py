from collections import defaultdict

s = input()
t = input()

s_dict = defaultdict(list)
t_dict = defaultdict(list)
for i in range(len(s)):
    s_dict[s[i]].append(i)
    t_dict[t[i]].append(i)
s_alph = [False] * 26
for i in range(len(s)):
    if not s_alph[ord(s[i]) - ord("a")]:
        if s_dict[s[i]] != t_dict[t[i]]:
            print("No")
            quit()
        else:
            s_alph[ord(s[i]) - ord("a")] = True
print("Yes")
