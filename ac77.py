def comparar_str(x1, x2):
    if len(x1) != len(x2):
        return len(x1) - len(x2)
    else:
        return 0

g = int(input())


casoteste = []

for _ in range(g):
    strings = input().split()
    casoteste.append(strings)

for strings in casoteste:
    strings.sort(key=lambda x: (len(x), strings.index(x)))

for strings in casoteste:
    print(*strings)