import sys
sys.stdin = open('1219.txt')

def dfs(now):
    visited[now] = 1
    for nxt in graph[now]:          # 현재 노드의 간선 탐색
        if not visited[nxt]:        # 만약 방문 안했다면
            dfs(nxt)                # 더 탐색

for tc in range(1, 11):
    T, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(0, 2 * E, 2):
        graph[arr[i]].append(arr[i + 1])
    visited = [0] * 100
    dfs(0)
    print(f'#{tc} {visited[99]}')