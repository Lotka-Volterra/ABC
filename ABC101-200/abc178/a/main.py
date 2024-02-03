x = int(input())
tf = '10'
print(tf[x])

# NOTは~ XORは^
# ~xを&を使って1桁（0b1)に限定することで、Pythonの~による符号の逆転を無視できる
print(int(~x & 0b1))
print(1-x)
# 1とXORをとることで、反転
print(1 ^ x)
