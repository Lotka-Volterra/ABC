class TreeNode:
    def __init__(self, number, x, y):
        self.number = number  # 人の番号
        self.x = x  # X座標
        self.y = y  # Y座標
        self.children = []  # 子ノードのリスト

# 人1の情報
person1 = TreeNode(1, 0, 0)

# # 人2の情報
# person2 = TreeNode(2, 2, 1)

# # 人3の情報
# person3 = TreeNode(3, -1, -2)

# # 人2から見た人4の情報
# person4 = TreeNode(4, 2 - 3, 1 - 2)
n,m= map(int,input().split())
for i in range(n):
    a,b,x,y= map(int,input().split())
    
# グラフを構築する
person1.children.extend([person2, person3])
person2.children.append(person4)

# グラフの葉に各人の情報が含まれています
# 例えば、人1の情報は以下のようにアクセスできます:
# person1.number, person1.x, person1.y

# グラフの探索を行い、各人の情報を表示する例
def traverse_tree(node):
    if node is None:
        return
    print(f"Person {node.number}: (X: {node.x}, Y: {node.y})")
    for child in node.children:
        traverse_tree(child)

# グラフの探索を実行
traverse_tree(person1)
