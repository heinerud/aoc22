from pathlib import Path


G = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
WIN = {3: 2, 2: 1, 1: 3}
LOSE = {1: 2, 2: 3, 3: 1}


def play(opponent, player):
    if (player, opponent) in WIN.items():
        return player + 6
    elif opponent == player:
        return player + 3

    return player


def strategy(opponent, player):
    if player == 1:
        return WIN[opponent]
    elif player == 2:
        return opponent
    else:
        return LOSE[opponent]


def main():
    day = Path(__file__).stem
    with open(f"{day}.in") as f:
        rounds = [l.split() for l in f.readlines()]

    print(sum(play(G[a], G[b]) for a, b in rounds))
    print(sum(play(G[a], strategy(G[a], G[b])) for a, b in rounds))


if __name__ == "__main__":
    main()
