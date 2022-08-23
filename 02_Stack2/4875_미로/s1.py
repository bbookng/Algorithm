import sys
sys.stdin = open('4875.txt')
sys.setrecursionlimit(10000)

def dfs(x, y):
    global flag
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                dfs(nx, ny)
            elif arr[nx][ny] == 3:
                flag = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = 0

    for i in range(N):
        for j in arr[i]:
            if j == 2:
                x = i
                y = arr[i].index(2)

    dfs(x, y)
    print(f'#{tc} {flag}')

