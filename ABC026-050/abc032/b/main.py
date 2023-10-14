s = input()
k = int(input())
password = []
for i in range(len(s) - k + 1):
    password.append(s[i : i + k])
print(len(list(set(password))))
