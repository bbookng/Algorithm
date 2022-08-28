import sys
sys.stdin = open('9489.txt')

def sol(N, M, site):
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if site[i][j] == 1:
                cnt += 1
                if cnt > result:
                    result = cnt
            else:
                cnt = 0
    for i in range(M):
        cnt = 0
        for j in range(N):
            if site[j][i] == 1:
                cnt += 1
                if cnt > result:
                    result = cnt
            else:
                cnt = 0

    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    site = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {sol(N, M, site)}')