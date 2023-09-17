from decimal import ROUND_HALF_UP, Decimal
print(Decimal(input()).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
