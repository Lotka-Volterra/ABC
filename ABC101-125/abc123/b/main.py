def change(i):
    return 10 if i % 10 == 0 else i % 10


dishes = []
for i in range(5):
    a = int(input())
    dishes.append([change(a), a])
# mod10が小さいかつmod10!=0の料理を最後の注文にする
dishes.sort(reverse=True)
ans = 0
for i in range(4):
    ans += dishes[i][1] + (10 - dishes[i][0])
ans += dishes[4][1]
print(ans)
