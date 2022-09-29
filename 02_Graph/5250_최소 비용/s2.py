# 130ms

import sys, heapq
sys.stdin = open('input.txt')

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp = 1
                if arr[nx][ny] > arr[x][y]:
                    tmp += (arr[nx][ny] - arr[x][y])
                cost = dist + tmp
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]

    dijkstra()
    print(f'#{tc} {distance[N-1][N-1]}')