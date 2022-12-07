with open("04.in") as f:
    lines = [l.strip() for l in f.readlines()]

p1 = p2 = 0
for l in lines:
    a, b, c, d = [int(x) for x in l.replace(",", "-").split("-")]
    A, B = set(range(a, b + 1)), set(range(c, d + 1))

    if A.issubset(B) or B.issubset(A):
        p1 += 1

    if not A.isdisjoint(B):
        p2 += 1

print(p1, p2)
