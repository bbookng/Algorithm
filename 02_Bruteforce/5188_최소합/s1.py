import sys
sys.stdin = open('input.txt')

def dfs(x, y, total):
    global result
    if total > result:
        return
    if x == N-1 and y == N-1:
        result = total
        return
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, total + arr[nx][ny])
            visited[nx][ny] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 9999999
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')
