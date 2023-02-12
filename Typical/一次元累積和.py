#n日間続くイベントがある。l日目からr日目までの来場者の総数について、q個の質問に答える。
n, q = map(int, input().split())
#1日目からn日目の各日の来場者数のリストa
a = list(map(int, input().split()))
#0日目からn日目までn+1日分用意
visitorsum = [0]*(n+1)

#visitorsumに、i日目までの累積来場者数を格納
for i in range(1,n+1):
    visitorsum[i]=visitorsum[i-1]+a[i]
#
for j in range(q):
    l, r = map(int, input().split())
    #r日目までの累積来場者数からl-1日目までの累積来場者数を引いて、l日目からr日目までの間の累積来場者数を出力
    print(visitorsum[r]-visitorsum[l-1])
