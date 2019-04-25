a = [2,4,6,8]
b = [1,3,5,7,9]
s=[1]
c = [1+r for a, r in zip(a + s, s+a)]
print(a)
print(b)
print(c)