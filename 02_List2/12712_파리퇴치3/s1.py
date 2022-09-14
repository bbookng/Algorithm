import sys
sys.stdin = open('12712.txt')

def sol(N, M, board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = 0

    for i in range(N):
        for j in range(N):
            sums = 0
            sums += board[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx, ny = i + dx[k] * l, j + dy[k] * l
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    sums += board[nx][ny]
            if sums > result:
                result = sums

    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            sums = 0
            sums += board[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx, ny = i + dx[k] * l, j + dy[k] * l
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    sums += board[nx][ny]
            if sums > result:
                result = sums
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int , input().split())) for _ in range(N)]
    print(f'#{tc} {sol(N, M, board)}')
