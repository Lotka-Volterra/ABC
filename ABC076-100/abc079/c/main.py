s = input()
for i in range(2):
    for j in range(2):
        for k in range(2):
            abcd = int(s[0])
            ans = s[0]
            if i == 0:
                abcd += int(s[1])
                ans += "+" + s[1]
            else:
                abcd -= int(s[1])
                ans += "-" + s[1]
            if j == 0:
                abcd += int(s[2])
                ans += "+" + s[2]
            else:
                abcd -= int(s[2])
                ans += "-" + s[2]
            if k == 0:
                abcd += int(s[3])
                ans += "+" + s[3]
            else:
                abcd -= int(s[3])
                ans += "-" + s[3]
            if abcd == 7:
                ans += "=7"
                print(ans)
                quit()
