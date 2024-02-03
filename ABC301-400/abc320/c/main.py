n = int(input())
s1 = input()
s2 = input()
s3 =input()
slot = [[[], [], []] for i in range(10)]
for i in range(n):
    slot[int(int(s1[i]))-1][0].append(i)
for i in range(n):
    slot[int(s2[i])-1][1].append(i)
for i in range(n):
    slot[int(s3[i])-1][2].append(i)
for i in range(n):
    if len(slot[int(int(s1[i]))-1][0])==1:
        slot[int(int(s1[i]))-1][0].append(slot[int(int(s1[i]))-1][0][0]+n)
        slot[int(s1[i])-1][0].append(slot[int(s1[i])-1][0][0]+2*n)
    elif len(slot[int(s1[i])-1][0])==2:
        slot[int(s1[i])-1][0].append(slot[int(s1[i])-1][0][0]+n)
for i in range(n):
    if len(slot[int(s2[i])-1][1])==1:
        slot[int(s2[i])-1][1].append(slot[int(s2[i])-1][1][0]+n)
        slot[int(s2[i])-1][1].append(slot[int(s2[i])-1][1][0]+2*n)
    elif len(slot[int(s2[i])-1][1])==2:
        slot[int(s2[i])-1][1].append(slot[int(s2[i])-1][1][0]+n)
for i in range(n):
    if len(slot[int(s3[i])-1][2])==1:
        slot[int(s3[i])-1][2].append(slot[int(s3[i])-1][2][0]+n)
        slot[int(s3[i])-1][2].append(slot[int(s3[i])-1][2][0]+2*n)
    elif len(slot[int(s3[i])-1][2])==2:
        slot[int(s3[i])-1][2].append(slot[int(s3[i])-1][2][0]+n)
# for j in range(min(len(slot[i][0])),3):
#     for k in range(min(len(slot[i][1])),3):
#         for l in range(min(len(slot[i][2])),3):
min_sum = 301 # 最小合計を無限大で初期化
# min_num = 301
for i in range(10):
    for a in slot[i][0]:
        for b in slot[i][1]:
            for c in slot[i][2]:
                # 3つの整数が重複しないか確認
                if len(set([a, b, c])) == 3:
                    # print(a,b,c)
                    current_sum = max(a,b,c)
                    if current_sum < min_sum:
                        min_sum = current_sum
                        min_num = i
if min_sum == 301:
    print(-1)
else:
    print(min_sum)