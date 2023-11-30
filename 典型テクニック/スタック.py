from collections import deque
q = int(input())
stack = deque()
for i in range(q):
    query = list(input().split())
    # スタックの１番上に追加
    if query[0] == '1':
        stack.append(query[1])
    # スタックの一番上を表示
    elif query[0] == '2':
        print(stack[-1])
    # スタックの一番上を削除（一番上の要素も返す。受け取る場合はs=stack.pop()で受け取る）
    else:
        stack.pop()
