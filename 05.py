def stack_setup(lines):
    stack_lines = []
    for l in lines:
        if not l:
            break
        stack_lines.append(l)

    *crate_lines, stack_numbers = stack_lines
    num_stacks = int(stack_numbers[-1])

    stacks = []
    for i in range(num_stacks):
        crates = []
        for l in reversed(crate_lines):
            try:
                c = l[i * 4 + 1]
                if c != " ":
                    crates.append(c)
            except IndexError:
                pass
        stacks.append(crates)

    return stacks


def main():
    with open("05.in") as f:
        lines = [l.rstrip() for l in f.readlines()]

    stacks_p1 = stack_setup(lines)
    stacks_p2 = stack_setup(lines)
    for l in (l for l in lines if l.startswith("move")):
        _, n, _, source, _, target = l.split()
        n, source, target = int(n), int(source) - 1, int(target) - 1

        for _ in range(n):
            stacks_p1[target].append(stacks_p1[source].pop())

        for i in reversed(range(n)):
            stacks_p2[target].append(stacks_p2[source].pop((i + 1) * -1))

    for s in stacks_p1:
        print(s[-1], end="")

    print()

    for s in stacks_p2:
        print(s[-1], end="")


if __name__ == "__main__":
    main()
