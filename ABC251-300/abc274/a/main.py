a, b = map(int, input().split())
ans = str(b * (10**4) // a)
# print(ans)
if a == b:
    print("1.000")
else:
    if int(str(ans[-1])) > 4:
        ans = str(int(ans) + 10)
    ans = "0" * (5 - len(str(ans))) + str(ans)    
    print(f"{ans[0]}.{ans[1:4]}")
