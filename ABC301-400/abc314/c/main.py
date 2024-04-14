from collections import defaultdict

n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))
# 色ごとに出現する文字を（前から）出現する順番でリストに格納
color = defaultdict(list)
for i in range(n):
    color[c[i]].append(s[i])
for k, v in color.items():
    # 文字のリストを1つずらす
    color[k] = [color[k][-1]] + color[k]
# 色ごとのリストのインデックスを辞書で管理。前から順番にansに格納
color_index = defaultdict(int)
ans = []
for i in range(n):
    ans.append(color[c[i]][color_index[c[i]]])
    color_index[c[i]] += 1
print("".join(ans))
