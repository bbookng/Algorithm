import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home = []
    service = [i*i+(i-1)**2 for i in range(N+2)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))

    result = 0
    for k in range(1, N+2):
        for i in range(N):
            for j in range(N):
                tmp = 0
                for x, y in home:
                   if abs(i-x) + abs(j-y) < k:
                       tmp += 1
                if tmp * M - service[k] >= 0 and tmp > result:
                    result = tmp

    print(f'#{tc} {result}')



