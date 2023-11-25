list = list(input().split())
w = ''
for i in list:
    w += i[0].upper()
print(w)

#関数を使わない場合、C++なら以下のように文字コードの差を求めて大文字化できる  
""" int main (){
string a , b , c ;
cin >> a >> b >> c ;
char dif = ’A ’ - ’a ’;
printf ("% c % c % c \ n " , a [0] + dif , b [0] + dif , c [0] + dif );
return 0;
} """