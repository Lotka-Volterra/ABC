s = input()
count = 0
for i in range(3):
    if s[i] == "1":
        count += 1
print(count)

#別解　strをlistにすることで文字をバラバラにし、それをintにする。要素は１か０なので、要素の合計を出す
nm = list(map(int, list(str(input()))))
print(sum(nm))
#別解　１の数を数える
print(s.count('1'))