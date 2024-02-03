import math


def pay(price, count):
    for i in range(1, 11):
        factI = math.factorial(i)
        if factI == price:
            print(count + 1)
            quit()
        elif factI > price:
            factI1 = math.factorial(i - 1)
            count += price // factI1
            price -= factI1 * (price // factI1)
            if price == 0:
                print(count)
                quit()
            else:
                pay(price, count)
        # factorial(10)<priceのとき
        elif i == 10:
            count += price // factI
            price -= factI * (price // factI)
            if price == 0:
                print(count)
                quit()
            else:
                pay(price, count)


price = int(input())
pay(price, 0)
