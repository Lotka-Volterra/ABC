n,m=  map(int,input().split())
# ab=[]
# alist=[0]*n
# for i in range(m):
#     a,b= map(int,input().split())
#     ab.append([a,b])
#     alist[a-1]+=1
# ab.sort()
# print(ab)
# print(alist)

# TODO:途中。グラフを作って、ある頂点からつながる頂点を渡っていき、つながる頂点がn-1個であればそれが一番強いと判断するという方針。
graph = [[]]*n
# print(graph)
for i in range(m):
    a,b= map(int,input().split())
    graph[a-1].append(b-1)
    print(graph)
print(graph)
