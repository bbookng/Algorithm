import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(x):
    q = [x]
    while q:
        n = q.pop()
        if not visited[n]:
            visited[n] = 1
            for i in graph[n]:
                if not visited[i]:
                    q.append(i)





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])

    visited = [0] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')
