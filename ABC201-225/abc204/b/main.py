N = int(input())
A = list(map(int,input().split()))
count = 0
for i in range(N):
    if A[i]<=10:
        continue
    else:
        count+=A[i]-10
print(count)

# continueするところはいらなかった
# if A[i]>10: count+=A[i]-10だけでよかった
#別解
#count += max(0, A[i] - 10);