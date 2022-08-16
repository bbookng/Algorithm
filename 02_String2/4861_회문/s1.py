import sys
sys.stdin = open('4861.txt')

def sol(N, M, arr):
    for i in range(N):
        for j in range(N-M+1):
            row = []
            col = []
            for k in range(M):
                row.append(arr[i][j+k])
                col.append(arr[j+k][i])
            if row == row[::-1]:
                return row
            elif col == col[::-1]:
                return col

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    result = ''.join(sol(N, M, arr))
    print(f'#{tc} {result}')