import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
line = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

def bfs(a, b):
    Q = deque([])
    Q.append((a, b))
    visited[a][b] = 1
    while Q:
        x, y = Q.popleft()
        tmp = line[board[x][y]]
        if not tmp:
            continue
        for i in tmp:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                tmp = line[board[nx][ny]]
                for j in tmp:
                    nx2 = nx + dx[j]
                    ny2 = ny + dy[j]
                    if x == nx2 and y == ny2:
                        visited[nx][ny] = visited[x][y] + 1
                        Q.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')



