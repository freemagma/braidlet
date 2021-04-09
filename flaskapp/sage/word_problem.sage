import sys

b1 = [int(x) for x in sys.argv[1].split(",")]
n = max(map(abs, b1))
B = BraidGroup(n)

b1 = B(b1)
b2 = B([])

print(b1 == b2)