#方針：要素がすべて０のリストを作り、０から９の出現フラグに対応させる。
#0なら出現していない、１なら出現した。要素が０のままのインデックス＝出現していない数
S = input()
S_list = [0]*10
for i in S:
    S_list[int(i)] += 1
for i in range(10):
    if S_list[i]==0:
        print(i)

#公式解答
S=input()
flag=[True for i in range(10)]
for i in range(9):
	flag[int(S[i])]=False
for i in range(10) :
	if(flag[i]):
		print(i)
#また、余談ですが、0+1+⋯+9=45 から登場した数字をすべて引く事でも答えを求めることができます。 
list_ = list(map(int, list(input()) ))
print(45-sum(list_))
#pythonの最速処理解答
S = input()
for i in range(10):
    i_str = str(i)
    if i_str in S:
        continue
    else:
        print(i)
        exit()