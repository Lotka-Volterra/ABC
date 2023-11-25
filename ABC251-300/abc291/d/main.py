n= int(input())
ab=[]
for i in range(n):
    a,b= map(int,input().split())
    ab.append([a,b])
tf=[0]*n
tf[0]=2
dp=[0]*n
dp[0]=2
for i in range(1,n):
    if tf[i-1]==2:
        # i番目の表はi-1の表裏と異なる
        if ab[i][0]!=ab[i-1][0] and ab[i][0]!=ab[i-1][1]:
            # i番目の裏はi-1の表裏と異なる
            if ab[i][1]!=ab[i-1][0] and ab[i][1]!=ab[i-1][1]:
                dp[i]=dp[i-1]+2
                tf[i]=2
            # i番目の裏はi-1の表裏の一方と異なる
            elif ab[i][1]!=ab[i-1][0] or ab[i][1]!=ab[i-1][1]:
                dp[i]=dp[i-1]+1
                tf[i]=2
            # i番目の裏はi-1の表裏と一致
            elif ab[i][1]!=ab[i-1][0] or ab[i][1]!=ab[i-1][1]:
                dp[i]=dp[i-1]
                tf[i]=0
        # ここからは、iの表はi-1の表裏の少なくとも一方と同じ
        elif ab[i][0]!=ab[i-1][0] or ab[i][1]==ab[i-1][0]:
            # i番目の裏はi-1の表裏と異なる
            if ab[i][1]!=ab[i-1][0] and ab[i][1]!=ab[i-1][1]:
                dp[i]=dp[i-1]+1
                tf[i]=2
            # i番目の裏はi-1の表裏の一方と異なる
            elif ab[i][1]!=ab[i-1][0] or ab[i][1]!=ab[i-1][1]:
                dp[i]=dp[i-1]
                tf[i]=2
            # i番目の裏はi-1の表裏の両方と同じ
            elif ab[i][1]==ab[i-1][0] and ab[i][1]==ab[i-1][1]:
                dp[i]=dp[i-1]-1
                tf[i]=0
            dp[i]=dp[i-1]
            tf[i]=0
        # iの表はi-1の表裏の両方と同じ
        # iの裏はi-1の表裏のいずれとも異なる
        elif ab[i][1]!=ab[i-1][0] and ab[i][1]!=ab[i-1][1]:
            dp[i]=dp[i-1]
            tf[i]=1
        # iの裏はi-1の表裏のいずれかと異なる
        elif ab[i][1]!=ab[i-1][0] or ab[i][1]!=ab[i-1][1]:
            dp[i]=dp[i-1]-1
            tf[i]=1
        # iの表裏にi-1の表裏と異なる数字はない
        else:
            print(0)
            quit()
    elif tf[i-1]==1:
        # iの表裏はいずれもi-1の裏と異なる
        if ab[i][0]!=ab[i-1][1] and ab[i][1]!=ab[i-1][1]:
            dp[i]=dp[i-1]+1
            tf[i]=2
        elif ab[i][0]!=ab[i-1][1] and ab[i][1]==ab[i-1][1]:
            dp[i]=dp[i-1]
            tf[i]=0
        elif ab[i][0]==ab[i-1][1] and ab[i][1]!=ab[i-1][1]:
            dp[i]=dp[i-1]
            tf[i]=1
        else:
            print(0)
            quit()
    elif tf[i-1]==0:
        if ab[i][0]!=ab[i-1][0] and ab[i][1]!=ab[i-1][0]:
            dp[i]=dp[i-1]+1
            tf[i]=2
        elif ab[i][0]!=ab[i-1][0] and ab[i][1]==ab[i-1][0]:
            dp[i]=dp[i-1]
            tf[i]=0
        elif ab[i][0]==ab[i-1][0] and ab[i][1]!=ab[i-1][0]:
            dp[i]=dp[i-1]
            tf[i]=1
        else:
            print(0)
            quit()
print(dp[n-1]%998244353)