import sys
sys.stdin = open('p3.txt')

E, V = map(int,input().split())
arr = list(map(int,input().split()))

graph = [[] for _ in range(8)]

for i in range(0, 2 * V, 2):
    graph[arr[i]].append(arr[i + 1])
    graph[arr[i + 1]].append(arr[i])

def dfs():
    start = 1
    q = [start]
    visited = [0] * 8
    answer = []

    while q:
        now = q.pop()
        visited[now] = 1
        answer.append(now)

        for nxt in graph[now]:
            if not visited[nxt] and nxt not in q:
                q.append(nxt)

    return answer

print(dfs())

visited = [0] * 8
def dfs2(now):
    visited[now] = 1
    print(now, end=" ")
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs2(nxt)

dfs2(1)