import sys
sys.stdin = open('4869.txt')

def sol(N):
    N = N//10
    dp =[0] * (N+1)
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] * 2 + 1 if i % 2 == 0 else dp[i-1] * 2 - 1
    return dp[i]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {sol(N)}')