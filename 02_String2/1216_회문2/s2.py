import sys
sys.stdin = open('1216.txt')

def solution(arr):
    for k in range(100, 0, -1):
        if len(sol(arr)) == k:
            return k

def sol(arr):
    for i in range(100):
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
    arr = [sys.stdin.read() for i in range(100)]
    result = solution(arr)
    print(f'#{tc} {result}')