import copy


def saiki(templist, numlist):
    if len(numlist) == 0:
        ans.append(templist)
        return
    for i in numlist:
        copytemplist = copy.deepcopy(templist)
        copytemplist.append(i)
        copynumlist = copy.deepcopy(numlist)
        copynumlist.remove(i)
        # print(copynumlist)
        saiki(copytemplist, copynumlist)


n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
numlist = list(range(1, n + 1))
ans = []
saiki([], numlist)
# print(ans)
pind = 0
qind = 0
for i in range(len(ans)):
    if ans[i] == p:
        pind = i
    if ans[i] == q:
        qind = i
print(abs(pind - qind))
