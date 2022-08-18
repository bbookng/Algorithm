import sys
sys.stdin = open('4871.txt')


def dfs(now):
    visited[now] = 1
    for nxt in graph[now]:          # 현재 노드의 간선 탐색
        if not visited[nxt]:        # 만약 방문 안했다면
            dfs(nxt)                # 더 탐색


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for i in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in arr:
        graph[i[0]].append(i[1])
    visited = [0] * (V+1)
    dfs(S)
    print(f'#{tc} {visited[G]}')

