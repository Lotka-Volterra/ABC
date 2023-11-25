n = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(n):
    s = input()
    if s == "AC":
        ac += 1
    elif s == "WA":
        wa += 1
    elif s == "TLE":
        tle += 1
    else:
        re += 1
print("AC x {0}".format(ac))
print("WA x {0}".format(wa))
print("TLE x {0}".format(tle))
print("RE x {0}".format(re))
