import sys
sys.stdin = open('input.txt')

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
                    if graph[i][j] > 0 and MST[j] == 0 and minV > graph[i][j]:
                        u = j
                        minV = graph[i][j]
        s += minV
        MST[u] = 1
    return s

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    print(f'#{tc} {prim2(0, V)}')