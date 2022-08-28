import sys
sys.stdin = open('9489.txt')


T = int(input())

def sol(n, m, arr):
    max_ = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                if max_ < cnt:
                    max_ = cnt
            else:
                cnt = 0
    for i in range(m):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
                if max_ < cnt:
                    max_ = cnt
            else:
                cnt = 0
    return max_


for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    print(f'#{tc} {sol(n, m, arr)}')