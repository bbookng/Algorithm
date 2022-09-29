# 2730ms

import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(S, ajdM):
    dp = [float('inf')] * (N+1)
    visited = [0] * (N+1)
    q = []
    heapq.heappush(q, (0, S))
    while q:
        time, now = heapq.heappop(q)
        if visited[now]:
            continue
        visited[now] = 1
        dp[now] = time
        for i in range(1, N+1):
            if not visited[i]:
                dp[i] = min(dp[i], time + ajdM[now][i])
                heapq.heappush(q, (dp[i], i))
    return dp

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[1000000] * (N+1) for _ in range(N+1)]
    adj2 = [[1000000] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        adj1[i][i] = 0
        adj2[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    dp1 = dijkstra(X, adj1)
    dp2 = dijkstra(X, adj2)

    max_ = 0

    for i in range(1, N+1):
        max_ = max(max_, dp1[i] + dp2[i])

    print(f'#{tc} {max_}')