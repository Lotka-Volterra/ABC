from collections import deque
q = int(input())
que = deque()
for i in range(q):
    query = list(input().split())
    # キューの最後尾（最新）に追加
    if query[0] == '1':
        que.append(query[1])
    # キューの先頭（最古）を表示
    elif query[0] == '2':
        print(que[0])
    # キューの先頭（最古）を削除（先頭の要素も返す。受け取る場合はq=que.popleft()で受け取る）
    else:
        que.popleft()
