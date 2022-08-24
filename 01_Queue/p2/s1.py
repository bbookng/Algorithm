import sys
sys.stdin = open('input.txt')


V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(V+1)]

for i in range(0, E*2, 2):
    graph[arr[i]].append(arr[i+1])

def BFS(v, N):
    visited = [0] * (V + 1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

BFS(1, V)

