import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    cnt = 0
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] + 1 == arr[nx][ny]:
                q.append((nx, ny))
    return cnt



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    room = 0

    for i in range(N):
        for j in range(N):
            if bfs(i, j) > result:
                result = bfs(i, j)
                room = arr[i][j]
            elif bfs(i, j) == result:
                room = min(room, arr[i][j])


    print(f'#{tc} {room} {result}')

