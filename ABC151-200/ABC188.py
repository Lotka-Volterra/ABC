n,m = list(map(int,input().split()))

if (n-m)**2 >= 9:
    print("No")
else:
    print("Yes")

#別解：２数の最小値＋３と最大値の比較