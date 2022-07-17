n= int(input())
sa=2025-n
for i in range(1,10):
    for j in range(1,10):
        if i*j==sa:
            print(str(i),'x',str(j))
#制約条件が書いてあったので楽勝だったが、制約が広めに書いてある場合もある。
#2025という数字は、1*1から9*9を回して得るか、(1+2+3+...+9)*(1+2+3+...+9)=45*45を計算して得る
# 別解：約数を直接求める
n= int(input())
sa=2025-n
for i in range(1,10):
    if sa%i==0 and sa//i<10:
        print(i,'x',sa//i)