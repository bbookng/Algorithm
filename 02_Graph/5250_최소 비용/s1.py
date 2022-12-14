# 180ms

import sys
sys.stdin = open('input.txt')
from collections import deque


def solution():
    q = deque()
    q.append((0, 0))
    distance[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp = 1
                if arr[nx][ny] > arr[x][y]:
                    tmp += (arr[nx][ny] - arr[x][y])
                if distance[nx][ny] > distance[x][y] + tmp:
                    distance[nx][ny] = distance[x][y] + tmp
                    q.append((nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]

    solution()
    print(f'#{tc} {distance[N-1][N-1]}')