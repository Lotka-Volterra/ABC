n = int(input())
if n == 100:
    print("Perfect")
elif 90 <= n <= 99:
    print("Great")
elif 60 <= n <= 89:
    print("Good")
else:
    print("Bad")

#改善案　点数を高い順に判定しているので、範囲の最小値との比較だけでいい
N = int(input())
if N == 100:
    print("Perfect")
elif N >= 90:
    print("Great")
elif N >= 60:
    print("Good")
else:
    print("Bad")