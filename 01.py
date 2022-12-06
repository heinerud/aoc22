from pathlib import Path


def group(lines):
    G = []
    g = []

    for l in lines:
        if not l:
            G.append(g)
            g = []
        else:
            g.append(int(l))

    G.append(g)
    return G


if __name__ == "__main__":
    day = Path(__file__).stem
    with open(f"{day}.in") as f:
        lines = [l.strip() for l in f.readlines()]

    groups = group(lines)
    summed_groups = [sum(g) for g in groups]

    print(max(summed_groups))
    print(sum(sorted(summed_groups)[-3:]))
