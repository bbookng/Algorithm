import sys
sys.stdin = open('2001.txt')

def sol(n, m, arr):
    max_ = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp = 0
            for k in range(m):
                for l in range(m):
                    tmp += arr[i+k][j+l]
            if tmp > max_:
                max_ = tmp
    return max_

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {sol(n, m, arr)}')
