import math
a = int(input('输入正整数a……'))
b = int(input('输入正整数b……'))
gys = math.gcd(a,b)
gbs = a*b/gys
print('最大公约数是'+str(gys))
print('最小公倍数是'+str(gbs))
