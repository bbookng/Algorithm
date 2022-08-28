import sys
sys.stdin = open('1974.txt')

def sol(board):
    for i in range(9):
        check = []
        for j in range(9):
            if board[i].count(board[i][j]) > 1:
                return 0
            if not board[j][i] in check:
                check.append(board[j][i])
            else:
                return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []
            for k in range(3):
                for l in range(3):
                    if not board[i+k][j+l] in check:
                        check.append(board[i+k][j+l])
                    else:
                        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sol(board)}')