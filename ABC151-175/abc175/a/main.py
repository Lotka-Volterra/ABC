s = input()

if s == "RRR":
    print(3)
elif s[1:] == "RR" or s[0:2] == "RR":
    print(2)
elif "R" in s:
    print(1)
else:
    print(0)

# 別解
s = input()
sum = 0
l = []
for i in range(3):
    if s[i] == "R":
        sum += 1
    else:
        l.append(sum)
        sum = 0
l.append(sum)
print(max(l))

# 別解
s = input()
tsudukiflag = False
day = 0
days = []
for i in range(3):
    if s[i] == "R":
        if tsudukiflag == False:
            tsudukiflag = True
            day += 1
        else:
            day += 1
    else:
        days.append(day)
        day = 0
        tsudukiflag = False
days.append(day)
print(max(days))
