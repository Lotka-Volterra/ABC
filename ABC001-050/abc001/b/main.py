m = int(input())
if m < 100:
    print("00")
elif 100 <= m <= 5000:
    m//=100
    m = "0" * (2 - len(str(m))) + str(m)
    print(m)
elif 6000 <= m <= 30000:
    m//=1000
    print(m + 50)
elif 35000 <= m <= 70000:
    m//=1000
    print((m - 30) // 5 + 80)
else:
    print(89)
