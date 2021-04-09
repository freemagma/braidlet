import sys

b1 = [int(x) for x in sys.argv[1].split(",")]
b2 = [int(x) for x in sys.argv[2].split(",")]
n = max(max(map(abs, b1)), max(map(abs, b2)))
B = BraidGroup(n)

b1 = B(b1)
b2 = B(b2)

print(b1 == b2)