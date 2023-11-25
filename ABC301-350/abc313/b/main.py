# n, m = map(int, input().split())
# person = [[] for i in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     # person[a]に、aより弱い者を格納
#     person[a].append(b)
#     for j in range(1, n + 1):
#         # 推移律を再現（aより強い人はbより強い）
#         if a in person[j]:
#             person[j].append(b)
# for i in range(1, n + 1):
#     # 他のn-1人より強かったら最強
#     if len(person[i]) == n - 1:
#         print(i)
#         quit()
# print(-1)
# # 上記の方針でWA。多分、順序を考慮できていないのが問題(後から推移律が発覚しても反映できないので-1を出力している)
# # ex.1,2 3,4 2,3は全体を俯瞰すると1,2,3,4とわかるが順番に処理すると1が4より強いことがわからない
n, m = map(int, input().split())
person = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    # person[a]に、aより弱い者を格納
    person[a].append(b)
    person[a] = list(set(person[a] + person[b]))
    for j in range(1, n + 1):
        # 推移律を再現（aより強い人はbより強い）
        if a in person[j]:
            person[j] = list(set(person[j] + person[a]))
for i in range(1, n + 1):
    # 他のn-1人より強かったら最強
    if len(person[i]) == n - 1:
        print(i)
        quit()
print(-1)
