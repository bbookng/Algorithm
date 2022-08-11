import sys
sys.stdin = open('1979.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for c in range(n)]
    total = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n-1:
                if cnt == k:
                    total += 1
                cnt = 0

        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    total += 1
                cnt = 0
    print(f'#{tc} {total}')