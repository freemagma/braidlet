import sys

b1 = [int(x) for x in sys.argv[1].split(",")]
b2 = [int(x) for x in sys.argv[2].split(",")]
n = max(max(map(abs, b1)), max(map(abs, b2)))
B = BraidGroup(n)

b1 = B(b1)
b2 = B(b2)

if b1.is_conjugated(b2):
    conj = b2.conjugating_braid(b1)
    print(conj)
else:
    print("None")