import sys
sys.stdin = open('12712.txt')

def sol(M, board):
    center = N//2
    tmp1 = tmp2 = board[center][center]
    print(tmp1, tmp2)
    for i in range(1, M):
        if 0 <= center-i < N:
            tmp1 += board[center-i][center] + board[center+i][center] + board[center][center-i] + board[center][center+i]
            tmp2 += board[center-i][center-i] + board[center+i][center+i] + board[center+i][center-i] + board[center-i][center+i]
    return(max(tmp1, tmp2))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int , input().split())) for _ in range(N)]
    print(f'#{tc} {sol(M, board)}')
