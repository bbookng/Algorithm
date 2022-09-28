def prim2(r, V):
    MST = [0] * (V+1)       # MST 포함여부
    MST[r] = 1              # 시작정점 표시
    s = 0                   # MST 간선의 가중치 합

    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adjM = [[0] * (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(prim2(0, V))