from pathlib import Path


def priority(x):
    if x.islower():
        return ord(x) - 96
    else:
        return ord(x) - 38


def common(*sets):
    return list(set.intersection(*sets))[0]


def split_in_half(s):
    return s[: len(s) // 2], s[len(s) // 2 :]


def part1(lines):
    sum = 0
    for l in lines:
        a, b = split_in_half(l)
        sum += priority(common(set(a), set(b)))

    return sum


def part2(lines):
    if not lines:
        return 0

    a, b, c, *tail = lines
    return priority(common(set(a), set(b), set(c))) + part2(tail)


def main():
    day = Path(__file__).stem
    with open(f"{day}.in") as f:
        lines = [l.strip() for l in f.readlines()]

    p1 = part1(lines)
    print(p1)
    assert p1 == 7737

    p2 = part2(lines)
    print(p2)
    assert p2 == 2697


if __name__ == "__main__":
    main()
