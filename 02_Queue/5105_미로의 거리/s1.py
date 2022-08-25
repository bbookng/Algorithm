import sys
sys.stdin = open('5105.txt')

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    result = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1],[1, 0],[0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] == 0 :
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            elif 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] == 3 :
                visited[ni][nj] = visited[i][j]
                return visited[i][j] - 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j

    print(f'#{tc} {bfs(x, y, N)}')

