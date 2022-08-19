import sys
sys.stdin = open('4408.txt')

def sol(N):
    dp = [0] * 201
    for j in range(N):
        x, y = map(int, input().split())
        x = x // 2 if x % 2 == 0 else x // 2 + 1
        y = y // 2 if y % 2 == 0 else y // 2 + 1
        if x > y:
            x, y = y, x
        for k in range(x, y+1):
            dp[k] += 1
    return max(dp)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {sol(N)}')