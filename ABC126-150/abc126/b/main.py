s=input()
s01=int(s[:2])
s23=int(s[-2:])
if (s01>12 or s01==0) and 0<s23<=12:
    print('YYMM')
elif 0<s01<=12 and (s23>12 or s23==0):
    print('MMYY')
elif 0<s01<=12 and 0<s23<=12:
    print('AMBIGUOUS')
else:
    print('NA')