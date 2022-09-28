def prim1(r, V):
    MST = [0] * (V+1)
    key = [10000] * (V+1)
    key[r] = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)


V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(prim1(0, V))