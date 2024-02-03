s1 = input()
s2 = input()
s3 = input()
s = [s1, s2, s3]
t = input()
st = ""
for i in range(len(t)):
    ti = int(t[i])
    st += s[ti-1]
print(st)
