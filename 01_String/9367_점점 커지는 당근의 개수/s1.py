import sys
sys.stdin = open('9367.txt')

def sol(N, carrot):
    max_ = 1
    cnt = 1
    for i in range(1, N):
        if carrot[i] > carrot[i-1]:
            cnt += 1
            if cnt > max_:
                max_ = cnt
        else:
            cnt = 1
    return max_


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    print(f'#{tc} {sol(N, carrot)}')