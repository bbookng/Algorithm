import sys
from collections import deque
sys.stdin = open('5102.txt')

def BFS(v, N):
    visited = [0] * (V + 1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w == G:
                visited[w] = visited[v]
                return visited[w]
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1
    return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for a, b in arr:
        graph[a].append(b)
        graph[b].append(a)
    print(f'#{tc} {BFS(S, G)}')

