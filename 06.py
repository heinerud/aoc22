def marker(s, l):
    for i in range(len(s)):
        if len(set(s[i : i + l])) == l:
            return i + l


with open("06.in") as f:
    input = f.readline().strip()

print(marker(input, 4))
print(marker(input, 14))
