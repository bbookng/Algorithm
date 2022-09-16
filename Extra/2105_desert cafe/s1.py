import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(x, y, d, tmp):
    global result, i, j

    nx = x + dx[d]
    ny = y + dy[d]

    if d == 3 and nx == i and ny == j:
        # print(nx, i, ny, j, len(tmp))
        result = max(result, len(tmp))
        return

    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in tmp:
        # tmp.append(arr[nx][ny])
        # print(tmp)
        dfs(nx, ny, d, tmp + [arr[nx][ny]])

        if d != 3:
            dfs(nx, ny, d+1, tmp + [arr[nx][ny]])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1


    for i in range(N):
        for j in range(N):
            # tmp = [arr[i][j]]
            dfs(i, j, 0, [arr[i][j]])

    print(f'#{tc} {result}')
