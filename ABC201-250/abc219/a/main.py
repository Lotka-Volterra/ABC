x = int(input())
if x < 40:
    print(40-x)
elif x < 70:
    print(70-x)
elif x < 90:
    print(90-x)
else:
    print('expert')
    
#ループを用いて簡潔に実装することもできます。 40,70,90 のうち X より大きい最小のものを見つけ（存在しない場合は expert と出力）、その値から X を引くという処理を行っています。
point=[40,70,90]
for i in range(3):
    if x<point[i]:
        print(point[i]-x)
        quit()
print('expert')
