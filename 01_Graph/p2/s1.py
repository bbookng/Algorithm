import sys
sys.stdin = open('input.txt')

def bfs():
    visited = [0] * len(graph)
    q = []
    q.append(1)
    visited[1] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in graph[t]:
            if i and not visited[i]:
                visited[i] = 1
                q.append(i)

arr = list(map(int, input().split()))
graph = [[] for _ in range(len(arr)//2 + 1)]

for i in range(0, len(arr), 2):
    graph[arr[i]].append(arr[i+1])
    graph[arr[i+1]].append(arr[i])

bfs()
