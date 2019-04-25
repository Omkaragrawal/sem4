# pascal triangle

n = int(input("No. of rows"))

trow = [1]
y = [0]

for x in range(max(n, 0)):
    print(trow)
    trow = [1+r for l, r in zip(trow+y, y+trow)]
    n >= 1
