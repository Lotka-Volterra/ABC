n = list(map(int, input().split()))

if n[0] == n[1]:
    if n[2] == 0:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if  n[0] > n[1]:
        print("Takahashi")
    else:
        print("Aoki")