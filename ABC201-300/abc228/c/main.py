n, k = map(int, input().split())
p_list = []
for i in range(n):
    p1, p2, p3 = map(int, input().split())
    p_list.append(p1 + p2 + p3)
sorted_p_list = sorted(p_list, reverse=True)
point = sorted_p_list[k - 1]
for i in range(n):
    if p_list[i] + 300 >= point:
        print("Yes")
    else:
        print("No")
