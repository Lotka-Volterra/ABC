q = int(input())
associativeArray = {}
# リストを優先度付きキューに変換（要素が入っている既存リストの場合は必要、今回は空のリストなので実は不要）

for i in range(q):
    query = list(input().split())
    # 優先度付きキューに追加
    if query[0] == '1':
        associativeArray[query[1]]= int(query[2])
    # キューの最小要素を表示
    else:
        print(associativeArray[query[1]])
# 連想配列中に「key」というキーに紐づく値があるかどうか判定
# if (key in associativeArray):

